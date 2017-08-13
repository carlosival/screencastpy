import subprocess
import shlex


# This methodo get the default resolution of the screen automatic
def default_resolution():
    cmd = ['xrandr']
    cmd2 = ['grep', '*']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(cmd2, stdin=p.stdout, stdout=subprocess.PIPE)
    p.stdout.close()

    resolution_string, junk = p2.communicate()
    resolution = resolution_string.split()[0]

    return str(resolution, 'utf-8')


# First we define the default values of the main parameters
DEFAULT_RESOLUTION = default_resolution()
DEFAULT_CODEC = "h264"
DEFAULT_OUTPUTFILE = "output.avi"


def rec(resolution=DEFAULT_RESOLUTION, codec=DEFAULT_CODEC, outputfile=DEFAULT_OUTPUTFILE):
    # The command string that we'll execute. LOTS of manipulation here available!
    command = "ffmpeg -f x11grab -y -r 30 -s {resolution} -i :0.0 -vcodec {codec}  -f alsa -i default -ar 44100 -acodec libmp3lame -ac 2 {outputfile}".format(
        resolution=resolution, codec=codec, outputfile=outputfile)

    # Shlex functionality basically convert a "command" string in a array.
    arguments = shlex.split(command)

    # Call the subprocess  independently of the parent process.
    # Both can run without wait for the child conclude
    recprocess = subprocess.Popen(arguments, stderr=subprocess.DEVNULL, stdin=None, stdout=subprocess.DEVNULL,
                                  close_fds=True)

    # You can know the pid of the process no necesary for util for debug.
    # PID = recprocess.pid
    # print(PID)

    return recprocess


def stop(procrec):
    # Get the process and terminate.
    procrec.terminate()
    procrec.kill()

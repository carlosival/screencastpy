# Screencastpy

Utility for screencast Selenium Webdriver UI tests

### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
See deployment for notes on how to deploy the project on a live system.

#### Prerequisites

You need to install FFMEG software www.ffmpeg.org

Debian derivates
````
apt install ffmpeg
````
##### Install screencastpy

**Step 1** Install screencastpy
````
pip install screeencastpy
````
#### Example Usage 

**Step 1** Import screencastpy into you test
````
import screencastpy as record
````
**Step 2** configure configure screencastpy to record and stop at same time of test.

Code example xtest.py

 ````
    from selenium import webdriver
    import unittest
    import screencastpy as record

    
    class UItest(unittest.TestCase):
        
      def setUp(self):
         self.driver = webdriver.Chrome()
         self.driver.maximize_window()
         windowsize = self.driver.get_window_size()
         resolution = str(windowsize['width']) + 'x' + str(windowsize['height'])
         self.procrec = record.rec(resolution=resolution)
         self.driver.implicitly_wait(10)
        
      def test_X1(self):
         do something    
        
      def tearDown(self):
        record.stop(self.procrec)
        self.driver.quit()
 ````

### Note
````
This project have been tested in Linux only. If anyone can tested in any other enviroment please let us know.
````

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.


Authors

* **Carlos Martinez Ival** 
See also the list of contributors who participated in this project.

License

This project is licensed under the MIT License - see the LICENSE.md file for details

Acknowledgments

Thanks to these project, very good inspiration.

[PyRecordDesktop](https://github.com/Deusdies/PyRecordDesktop)
[RecordScreen](https://github.com/cessen/recordscreen)


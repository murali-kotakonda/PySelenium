



import unittest
from basics import commons
from selenium import webdriver

from basics.commons import getChromeDriver


class MyTest(unittest.TestCase):     # Create a class which is a childclass of unittest.testcase
    driver=None

    def setUp(self):
        print("setup function called")
        self.driver = getChromeDriver()

    def tearDown(self):
        print("teardown function is called")
        self.driver.close()
import unittest
from basics import commons
from selenium import webdriver
import time

from basics.commons import getChromeDriver


class MyTest(unittest.TestCase):     # Create a class which is a childclass of unittest.testcase

    def test1(self):                    # each instance method is a testcase.
        # get driver
        driver = getChromeDriver()

        # open google.com
        driver.get(commons.App_URL + "2.html")
        time.sleep(5)
        driver.close()

    def test2(self):
        # get driver
        driver = getChromeDriver()

        # open google.com
        driver.get(commons.App_URL + "3.html")
        time.sleep(5)
        driver.close()

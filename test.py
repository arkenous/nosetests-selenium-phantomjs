#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from distutils.spawn import find_executable
import os
from nose.tools import ok_

os.environ['PATH'] += ':/usr/local/bin'
phantomjs_path = find_executable('phantomjs', os.getenv('PATH'))


def test_sample1():
    driver = webdriver.PhantomJS()
    driver.get('https://www.google.com/')
    ok_('https://www.google' in driver.current_url)

    driver.close()


def test_sample2():
    driver = webdriver.PhantomJS()
    driver.get('http://www.google.co.jp/')
    ok_('https://www.trileg.net/' in driver.current_url)

    driver.close()

if __name__ == '__main__':
    test_sample1()
    test_sample2()

#!/usr/bin/env python

## Job Search Program

"""
This program opens the browser and searches a website and copies and parses data.

"""


### IMPORTS

import urllib, urllib2

from bs4 import BeautifulSoup

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


## Browser Opening

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

url = ('http://www.bch.org/careers/jobopportunities.aspx')
surl = ('http://www.bch.org/careers/jobopportunities.aspx') # url for selenium

ourUrl = opener.open(url).read()

soup = BeautifulSoup(ourUrl)

title = soup.title.text

## Selenium xpaths

mydriver = webdriver.Firefox()

xpaths = {'submitButton' : "//html/body/form/div[2]/input"
          }



if "Job opportunities" in title:
    print ("You are in  the right place")
    mydriver.find_element_by_xpath(xpaths['submitButton']).click()


else:
    print ("you are in the wrong place")



'''
Outfile Save

outfile = open("Jobs.txt", 'w')

outfile.write(ourUrl)
'''


##print(ourUrl)





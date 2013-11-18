'''

PROGRAM W/ SELENIUM, BEAUTIFULSOUP


'''
'''
    exempla good samaritan
    quest diagnostics
    labcorp
    WSi Healthcare
'''
# imports


import os, sys
import webbrowser
import urllib, urllib2
from urlparse import urlparse

from bs4 import BeautifulSoup


from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By




# URLS

url1 = 'https://www.healthcaresource.com/bch/index.cfm?&ijobpostondaysold=&template=dsp_job_list.cfm&ijobrowstart=1&fuseaction=search.jobList&ijobcatid=100'
url2 = ""

#open browser tab
opener = urllib2.build_opener()
mydriver = webdriver.Firefox()

# Save file

prog_data = open("prog_data.html", "w+")
prog_jobs = open("prog_jobs.txt", "a+")

# individual company defs

class Bch(object):
    '''
    SEARCHES BCH FOR JOBS
    '''
    
    def bch_site(self):
        
        mydriver.get(url1)
        bch_url = opener.open(url1).read()
        soup = BeautifulSoup(bch_url)
        title = soup.title.text
    
        if "HealthCareSource" in title:
            print ("You are in the BCH Server:\n JOBS:")
            #print (mydriver.page_source)
            

        else:
            print ("you are in the wrong place")

    def bch_parse(self):
        
        bch_parse = opener.open(url1).read()
        soup = BeautifulSoup(bch_parse)
        soup.prettify()
        for string in soup.strings:
            prog_data.write(repr(string))

        prog = open("prog_data.txt", "r")
        for line in prog:
            if "Laboratory" in line:
                print "Laboratory"
            elif "Laboratory Assistant" in line:
                print "Laboratory Assistant"

            else:
                print "No Jobs Found...bummer"
        prog.close()

    def bch_quit(self):
        mydriver.Quit()

class Exempla(object):
    ''' SEARCHES JOBS AT EXEMPLA GOOD SAMARITAN'''
'''
    def exe_site(self):
'''
        



    
# MAIN
def main():
    '''BCH'''
    Bch().bch_site()
    Bch().bch_parse()
    Bch().bch_quit()

main()

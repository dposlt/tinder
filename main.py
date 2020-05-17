#!/usr/bin/python env

__autohor__ = 'dposlt'
__email__ = 'david.poslt@gmail.com'
__licence__ = 'GPU'

import configparser, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#####################################
#####################################
##                                 ##
##   automatic choice for tinder   ##
##                                 ##
#####################################
#####################################

def readIni():
    config = configparser.ConfigParser()
    config.read('settings.ini')

    web = config['WEB']['page']
    user = config['SECURITY']['user']
    passwd = config['SECURITY']['password']
    driver = config['DRIVER']['webDriver']

    return web, user, passwd, driver

def checkFile():
    d = readIni()[3]
    if os.path.isfile(d):
        return d

def tinderPage():

    web,user,passwd, driver = readIni()
    browser = webdriver.Firefox(executable_path=checkFile())
    browser.get(web)

    login = browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/span/div[2]/button')
    login.click()

tinderPage()

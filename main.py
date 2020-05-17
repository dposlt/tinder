#!/usr/bin/python env

__autohor__ = 'dposlt'
__email__ = 'david.poslt@gmail.com'
__licence__ = 'GPU'

import configparser, os, time
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

    if browser:
        browser.get(web)
        time.sleep(5)

        ## login menu via fcb##

        try:
            browser.find_element_by_css_selector('button.Td\(u\):nth-child(3)').click()
        except:
            login = browser.find_element_by_css_selector('div.My\(10px\):nth-child(2) > button:nth-child(1)')
            login.click()


        ## Log In ##
        email = browser.find_element_by_css_selector('#email')
        email.text(user)
        password = browser.find_element_by_css_selector('#pass')
        password.text(passwd)

tinderPage()

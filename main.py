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

class TinderBot():

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=readIni()[3])


    def login(self):
        ## login via facebook ##
        web, user, passwd, driver = readIni()
        self.driver.get(web)

        time.sleep(4)

        if self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/span/div[2]/button').is_displayed():
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/span/div[2]/button').click()

        elif self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/span/div[3]/button').is_displayed():
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/span/div[3]/button').click()

        elif self.driver.find_element_by_xpath('html/body/div[2]/div/div/div/div/div[2]/span/div[2]/button').is_displayed():
            self.driver.find_element_by_xpath('html/body/div[2]/div/div/div/div/div[2]/span/div[2]/button').click()

        elif self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/span/button').is_displayed():
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/span/button').click()




        ## switch to login popup ##
        base_window = self.driver.window_handles[1]
        self.driver.switch_to.window(base_window)
        mail = self.driver.find_element_by_xpath('//*[@id="email"]')
        email.send_keys(user)

        pwd = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pwd.send_keys(passwd)



bot = TinderBot()

bot.login()

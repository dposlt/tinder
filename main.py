


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://www.youtube.com')

elemSearch = browser.find_element_by_name('search_query')
elemSearch.send_keys('selenium')

elemSearch.send_keys(Keys.ENTER)

browser.find_element_by_xpath('//*[@id="hover-overlays"]').click()
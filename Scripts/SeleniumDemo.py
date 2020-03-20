from selenium import webdriver
import sys
class SeleniumDemo:
    '''
    SeleniumDemo
    '''
    def demo(self):
        url = 'https://www.baidu.com'
        chrome = webdriver.Chrome()
        chrome.get(url)
        input = chrome.find_element_by_css_selector('#kw')
        input.send_keys('python')
        btn = chrome.find_element_by_css_selector('#su')
        btn.click()
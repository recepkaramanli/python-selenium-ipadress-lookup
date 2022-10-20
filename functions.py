from config import *
from selenium import webdriver as wd
from selenium.webdriver.common.by import By as by
import json


def find_location(browser, ip):
    data = {}
    try:
        browser.get(f"https://whatismyipaddress.com/ip/{ip}")
        get_value = lambda xpath: browser.find_element(by.XPATH, xpath)
        state = get_value(xpath_list[0])
        city = get_value(xpath_list[1])
        isp = get_value(xpath_list[2])
    except:
        data = {"error": "services not working"}
        pass
    data = {"ip": ip, "state": state.text, "city": city.text, "isp": isp.text}
    return json.dumps(data)



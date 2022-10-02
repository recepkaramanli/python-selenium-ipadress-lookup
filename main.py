from numpy import lookfor
from flask import Flask
from selenium import webdriver as wd
from selenium.webdriver.common.by import By as by

# tarayıcıyı aç hazır beklesin
browser = wd.Firefox(executable_path='./geckodriver.exe')
# browser = wd.Chrome(executable_path='./chromedriver.exe')
browser.minimize_window()

def lokasyon_bul(ip):
    data = {}
    try:
        browser.get('https://whatismyipaddress.com/ip/'+ip)
        state = browser.find_element(
        by.XPATH, '//*[@id="fl-post-1165"]/div/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[1]/p[8]/span[2]')
        city = browser.find_element(
        by.XPATH, '//*[@id="fl-post-1165"]/div/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[1]/p[9]/span[2]')        
        isp = browser.find_element(
            by.XPATH, '//*[@id="fl-post-1165"]/div/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[1]/p[4]/span[2]')
    except:
        data = {'error':'servis calismiyor'}
        pass
    data = {'ip':ip,'state':state.text,'city':city.text,'isp':isp.text}
    return data

app = Flask(__name__)
@app.route("/<ip>", methods=['GET'])  
def main(ip):
    return lokasyon_bul(ip)

app.run()
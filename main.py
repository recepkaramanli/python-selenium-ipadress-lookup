from flask import Flask
from selenium import webdriver as wd
from selenium.webdriver.common.by import By as by
import webbrowser
from functions import *
from config import *

options = wd.FirefoxOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
browser = wd.Firefox(executable_path=driver_path, options=options)
browser.minimize_window()

if __name__ == "__main__":
    app = Flask(__name__)

    @app.route("/<ip>", methods=["GET"])
    def query(ip):
        return find_location(browser, ip)

    @app.route("/")
    def index():
        return "working"

    webbrowser.open_new(f"http://localhost:{flask_port}")
    app.run(debug=flask_debug,port=flask_port)

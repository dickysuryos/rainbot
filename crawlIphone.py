from time import sleep
from selenium.webdriver.firefox.options import Options
import argparse
import psutil 
import os
from datetime import datetime
from selenium import webdriver

safari_options = webdriver.SafariOptions()
safari_options.set_capability("platformName", "iOS")
safari_options.set_capability("safari:deviceUDID", "00008120-000458422203C01E")
safari_options.set_capability("safari:deviceName", "iPhone 11")
safari_options.set_capability("browserName", "Safari")

# Create Safari webdriver with options
driver = webdriver.Safari(options=safari_options)
driver.get("https://detik.com/")
height = int(driver.execute_script("return document.body.scrollHeight"))
scrolls = int(height/300)
pos = 0
for i in range(300):
    driver.execute_script("window.scrollTo(0, " + str(pos) + ");")
    sleep(.5)
    pos += scrolls
driver.close()
date_at_end = datetime.now()
dt_string_end = date_at_end.strftime("%m/%d/%Y %H:%M:%S")
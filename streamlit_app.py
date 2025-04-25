from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import streamlit as st
import os

chrome_options = Options()
chrome_options.binary_location = "/usr/bin/chromium-browser"  # Update if different
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Properly create Service object
service = Service("/usr/local/bin/chromedriver")  # Path to your chromedriver

# Launch driver with service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# @st.cache_resource
# def get_driver():
#     service = Service(executable_path=os.path.join(os.getcwd(), "chromedriver"))
#     return webdriver.Chrome(service=service, options=options)

# driver = get_driver()
driver.get("https://find-and-update.company-information.service.gov.uk/")
st.code(driver.page_source)
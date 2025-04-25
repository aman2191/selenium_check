from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import streamlit as st
import os

options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/chromium-browser"
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=options)

# @st.cache_resource
# def get_driver():
#     service = Service(executable_path=os.path.join(os.getcwd(), "chromedriver"))
#     return webdriver.Chrome(service=service, options=options)

# driver = get_driver()
driver.get("https://find-and-update.company-information.service.gov.uk/")
st.code(driver.page_source)
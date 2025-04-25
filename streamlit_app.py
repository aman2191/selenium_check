from selenium.webdriver.chrome.options import Options
import streamlit as st
import undetected_chromedriver as uc

@st.cache_resource
def get_driver():
    options = uc.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return uc.Chrome(options=options)

driver = get_driver()
driver.get("https://find-and-update.company-information.service.gov.uk/")
st.code(driver.page_source)
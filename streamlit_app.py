import streamlit as st
from selenium import webdriver

def scrape_title(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)  
    driver.get(url)  
    title = driver.title  
    driver.quit()  
    return title

st.title("Chrome Web Scraping with Selenium")

url = st.text_input("Enter URL:")
if st.button("Scrape"):
    if url:
        st.write("Scraping title from:", url)
        title = scrape_title(url)
        st.write("Title:", title)
    else:
        st.write("Please enter a URL.")
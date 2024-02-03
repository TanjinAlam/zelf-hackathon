from helper.helper import all_user_profile_images, extract_user_profile_data_from_soup, take_screenshot
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
def get_each_user_stories(driver,url, email, password):
    driver.get(url)
    sleep(5)
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))
    )
    email_input.send_keys(email)
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'))
    )
    password_input.send_keys(password)
    driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
    sleep(10)
    driver.get('https://www.instagram.com/')
    sleep(5)
    driver.find_element(By.XPATH,"//button[contains(text(), 'Not Now')]").click()

    bs4_soup = BeautifulSoup(driver.page_source, 'html.parser')
    user_story_process_data = extract_user_profile_data_from_soup(bs4_soup)
    each_user_story_data = all_user_profile_images(driver,user_story_process_data)
    driver.quit()
    return each_user_story_data
    
    
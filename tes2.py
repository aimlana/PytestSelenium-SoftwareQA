import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_check_mikroskop(browser):
    lab_name = []

    browser.get("https://pyapp.unhas.ac.id/laboratorium")
    time.sleep(5)

    fakultas = browser.find_element(By.XPATH, '//*[@j=2]')
    fakultas.click()
    time.sleep(2)

    content = browser.find_element(By.XPATH, '//*[@id="fak_content"]/ul')
    time.sleep(2)

    labs = content.find_elements(By.TAG_NAME, 'a')

    for lab in labs:
        name = lab.text
        lab_name.append(name)

    for i in range(len(lab_name)):
        scroll_to_text = lab_name[i]
        elem = browser.find_element(By.PARTIAL_LINK_TEXT, scroll_to_text)
        browser.execute_script("arguments[0].scrollIntoView();", elem)
        time.sleep(2)

        to_lab = browser.find_element(By.PARTIAL_LINK_TEXT, lab_name[i])
        to_lab.click()
        time.sleep(2)

        ul_alat = browser.find_element(By.XPATH, '//*[@id="main_content"]/div/div/div[2]/ul[2]')
        li_alat = ul_alat.find_elements(By.TAG_NAME, 'li')

        lab_punya_mikroskop = False

        for li in li_alat:
            li_text = li.text
            browser.execute_script("arguments[0].scrollIntoView();", li)

            if "mikroskop" in li_text:
                lab_punya_mikroskop = True
        
        if lab_punya_mikroskop:
            print(f"lab_name: {lab_name[i]} -> ada mikroskop")
        else:
            print(f"lab_name: {lab_name[i]} -> tidak ada mikroskop")
                
        time.sleep(2)

        button = browser.find_element(By.XPATH, '//*[@id="main_content"]/div/div/div[1]/button')
        browser.execute_script("arguments[0].scrollIntoView();", button)
        time.sleep(2)
        button.click()
        time.sleep(4)
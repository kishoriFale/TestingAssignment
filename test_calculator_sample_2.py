from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
from openpyxl import load_workbook


def test_launch_browser():
    global driver
    s = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    sleep(1)
    driver.get("https://www.calculator.net/")


def test_read_excel_file():
    global sheet
    filepath = "sample_test_cases.xlsx"
    wb = load_workbook(filepath)
    sheet = wb.active


def test_multiplication():
    x = sheet['C1'].value
    driver.find_element(By.XPATH, '/html/body').send_keys(sheet['A1'].value)
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[4]').click()
    driver.find_element(By.XPATH, '/html/body').send_keys(sheet['B1'].value)
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[4]').click()
    webelement = driver.find_element(By.XPATH, '//*[@id="sciOutPut"]').text
    print(int(webelement))
    assert x == int(webelement)
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()
    sleep(2)


def test_division():
    x = sheet['C2'].value
    driver.find_element(By.XPATH, '/html/body').send_keys(sheet['A2'].value)
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[4]/span[4]').click()
    driver.find_element(By.XPATH, '/html/body').send_keys(sheet['B2'].value)
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[4]').click()
    webelement = driver.find_element(By.XPATH, '//*[@id="sciOutPut"]').text
    print(int(webelement))
    assert x == (int(webelement))
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()
    sleep(2)


def test_addition():
    x = sheet['C3'].value
    driver.find_element(By.XPATH, '/html/body').send_keys(sheet['A3'].value)
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[1]/span[4]').click()
    driver.find_element(By.XPATH, '/html/body').send_keys(sheet['B3'].value)
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[4]').click()
    webelement = driver.find_element(By.XPATH, '//*[@id="sciOutPut"]').text
    print(int(webelement))
    assert x == (int(webelement))
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()
    sleep(2)


def test_subtraction():
    x = sheet['C4'].value
    driver.find_element(By.XPATH, '/html/body').send_keys(sheet['A4'].value)
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[4]').click()
    driver.find_element(By.XPATH, '/html/body').send_keys(sheet['B4'].value)
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[4]').click()
    webelement = driver.find_element(By.XPATH, '//*[@id="sciOutPut"]').text
    print(int(webelement))
    assert x == (int(webelement))
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()
    sleep(2)


def test_close_browser():
    driver.close()


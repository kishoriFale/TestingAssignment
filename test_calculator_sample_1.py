from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep


def test_launch_browser():
    global driver
    s = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    sleep(1)
    driver.get("https://www.calculator.net/ ")


@pytest.mark.parametrize('num1,num2,expected_result', [(-234234, 345345, 111111)])
def test_addition(num1, num2, expected_result):
    x = expected_result
    driver.find_element(By.XPATH, '/html/body').send_keys(num1)
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[1]/span[4]').click()
    driver.find_element(By.XPATH, '/html/body').send_keys(num2)
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[4]').click()
    webelement = driver.find_element(By.XPATH, '//*[@id="sciOutPut"]').text
    print(int(webelement))
    assert x == (int(webelement))
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()
    sleep(2)


@pytest.mark.parametrize('num1,num2,expected_result', [(234823, -23094823, 23329646)])
def test_subtraction(num1, num2, expected_result):
    x = expected_result
    driver.find_element(By.XPATH, '/html/body').send_keys(num1)
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[4]').click()
    driver.find_element(By.XPATH, '/html/body').send_keys(num2)
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[4]').click()
    webelement = driver.find_element(By.XPATH, '//*[@id="sciOutPut"]').text
    print(int(webelement))
    assert x == (int(webelement))
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()
    sleep(2)


@pytest.mark.parametrize('num1,num2,expected_result', [(423, 525, 222075)])
def test_multiplication(num1, num2, expected_result):
    x = expected_result
    driver.find_element(By.XPATH, '/html/body').send_keys(num1)
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[4]').click()
    driver.find_element(By.XPATH, '/html/body').send_keys(num2)
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[4]').click()
    webelement = driver.find_element(By.XPATH, '//*[@id="sciOutPut"]').text
    print(int(webelement))
    assert x == (int(webelement))
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()
    sleep(2)


@pytest.mark.parametrize('num1,num2,expected_result', [(4000, 200, 20)])
def test_division(num1, num2, expected_result):
    x = expected_result
    driver.find_element(By.XPATH, '/html/body').send_keys(num1)
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[4]/span[4]').click()
    driver.find_element(By.XPATH, '/html/body').send_keys(num2)
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[4]').click()
    webelement = driver.find_element(By.XPATH, '//*[@id="sciOutPut"]').text
    print(int(webelement))
    assert x == (int(webelement))
    driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()
    sleep(2)


def test_close_browser():
    driver.close()


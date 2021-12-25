from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
from openpyxl import load_workbook
import unittest
import warnings


class TestCalculator(unittest.TestCase):

    def setUp(self):
        warnings.filterwarnings("ignore", category=ResourceWarning)
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        s = Service("chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        self.driver.get("https://www.calculator.net/")
        filepath = "sample_test_cases.xlsx"
        wb = load_workbook(filepath)
        self.sheet = wb.active


    def test_multiplication(self):
        x = self.sheet['C1'].value
        self.driver.find_element(By.XPATH, '/html/body').send_keys(self.sheet['A1'].value)
        self.driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[4]').click()
        self.driver.find_element(By.XPATH, '/html/body').send_keys(self.sheet['B1'].value)
        self.driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[4]').click()
        webelement = self.driver.find_element(By.XPATH, '//*[@id="sciOutPut"]').text
        print(int(webelement))
        assert x == (int(webelement))
        self.driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()
        sleep(2)
        # self.driver.close()


    def test_division(self):
        x = self.sheet['C2'].value
        self.driver.find_element(By.XPATH, '/html/body').send_keys(self.sheet['A2'].value)
        self.driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[4]/span[4]').click()
        self.driver.find_element(By.XPATH, '/html/body').send_keys(self.sheet['B2'].value)
        self.driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[4]').click()
        webelement = self.driver.find_element(By.XPATH, '//*[@id="sciOutPut"]').text
        print(int(webelement))
        assert x == (int(webelement))
        self.driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()
        sleep(2)


    def test_addition(self):
        x = self.sheet['C3'].value
        self.driver.find_element(By.XPATH, '/html/body').send_keys(self.sheet['A3'].value)
        self.driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[1]/span[4]').click()
        self.driver.find_element(By.XPATH, '/html/body').send_keys(self.sheet['B3'].value)
        self.driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[4]').click()
        webelement = self.driver.find_element(By.XPATH, '//*[@id="sciOutPut"]').text
        print(int(webelement))
        assert x == (int(webelement))
        self.driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()
        sleep(2)


    def test_subtraction(self):
        x = self.sheet['C4'].value
        self.driver.find_element(By.XPATH, '/html/body').send_keys(self.sheet['A4'].value)
        self.driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[4]').click()
        self.driver.find_element(By.XPATH, '/html/body').send_keys(self.sheet['B4'].value)
        self.driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[4]').click()
        webelement = self.driver.find_element(By.XPATH, '//*[@id="sciOutPut"]').text
        print(int(webelement))
        assert x == (int(webelement))
        self.driver.find_element(By.XPATH, '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()
        sleep(2)


    def tearDown(self):
        self.driver.close()

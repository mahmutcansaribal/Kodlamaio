# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCompleteShopping():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_completeShopping(self):
    self.driver.get("https://www.saucedemo.com/")
    WebDriverWait(self.driver, 1).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"username\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("perfonmance_glitch_user")
    WebDriverWait(self.driver, 1).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"password\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    WebDriverWait(self.driver, 1).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"login-button\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("performance_glitch_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    WebDriverWait(self.driver, 1).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    WebDriverWait(self.driver, 1).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "1")))
    self.driver.find_element(By.LINK_TEXT, "1").click()
    WebDriverWait(self.driver, 1).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"checkout\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]").click()
    WebDriverWait(self.driver, 1).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"firstName\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").send_keys("Mahmut Can")
    self.driver.find_element(By.CSS_SELECTOR, ".checkout_info").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").send_keys("Sarıbal")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").send_keys("34000")
    WebDriverWait(self.driver, 1).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"continue\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
    WebDriverWait(self.driver, 1).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"finish\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"finish\"]").click()
    WebDriverWait(self.driver, 1).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"back-to-products\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"back-to-products\"]").click()
    self.driver.close()
  

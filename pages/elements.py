import time

from selenium.webdriver.common.by import By


class Elements:
    def __init__(self, driver):
        self.driver = driver
        self.elements_box = "//h5[normalize-space()='Elements']"
        self.elements_heading = "//div[@class='main-header']"

    def verify_elements_main_page(self):
        button = self.driver.find_element(By.XPATH, self.elements_box)
        self.driver.execute_script('arguments[0].click()', button)
        time.sleep(10)
        return self.driver.find_element(By.XPATH, self.elements_heading).text



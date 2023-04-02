class LandingPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_landing_page(self):
        return self.driver.title

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SessionHelper:

    def __init__(self, app):
        self.app = app
    def login(self, user, password):
        app = self.app
        wd = app.wd
        app.open_home_page()
        wd.find_element(By.NAME, "user").send_keys(user)
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.NAME, "pass").send_keys(Keys.ENTER)

    def logout(self):
        app = self.app
        wd = app.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()

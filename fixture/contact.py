from selenium.webdriver.common.by import By


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        app = self.app
        wd = app.wd
        wd.find_element(By.LINK_TEXT, 'add new').click()
        for key, value in vars(contact).items():
            if value:
                wd.find_element(By.NAME, key).send_keys(value)
        wd.find_element(By.NAME, 'submit').click()

    def edit_first(self, contact):
        app = self.app
        wd = app.wd
        wd.find_element(By.XPATH, '//img[@title="Edit"]').click()
        for key, value in vars(contact).items():
            if value:
                wd.find_element(By.NAME, key).send_keys(value)
        wd.find_element(By.NAME, 'update').click()
        self.return_to_home_page()

    def delete_first(self):
        app = self.app
        wd = app.wd
        wd.find_element(By.NAME, 'selected[]').click()
        wd.find_element(By.XPATH, '//input[@value="Delete"]').click()
        wd.switch_to.alert.accept()

    def return_to_home_page(self):
        app = self.app
        wd = app.wd
        wd.find_element(By.LINK_TEXT, 'home page').click()

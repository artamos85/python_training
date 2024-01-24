from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.vars = {}

    def go_to_page(self, url):
        self.wd.get(url)

    def login(self, user, password):
        self.go_to_page("http://localhost/addressbook/")
        self.wd.find_element(By.NAME, "user").send_keys(user)
        self.wd.find_element(By.NAME, "pass").send_keys(password)
        self.wd.find_element(By.NAME, "pass").send_keys(Keys.ENTER)

    def logout(self):
        self.wd.find_element(By.LINK_TEXT, "Logout").click()

    def view_groups(self):
        self.wd.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, group):
        self.view_groups()
        self.wd.find_element(By.NAME, "new").click()
        self.wd.find_element(By.NAME, "group_name").send_keys(group.name)
        self.wd.find_element(By.NAME, "group_header").send_keys(group.header)
        self.wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        self.wd.find_element(By.NAME, "submit").click()

    def create_contact(self, contact):
        self.wd.find_element(By.LINK_TEXT, "add new").click()
        for key, value in vars(contact).items():
            if value:
                self.wd.find_element(By.NAME, key).send_keys(value)
        self.wd.find_element(By.NAME, "submit").click()

    def destroy(self):
        self.wd.quit()

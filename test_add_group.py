from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from group import Group


class TestAddGroup:
    def setup_method(self, method):
        self.wd = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.wd.quit()

    def go_to_page(self, url):
        self.wd.get(url)

    def login(self, user, password):
        self.wd.find_element(By.NAME, "user").send_keys(user)
        self.wd.find_element(By.NAME, "pass").send_keys(password)
        self.wd.find_element(By.NAME, "pass").send_keys(Keys.ENTER)

    def logout(self):
        self.wd.find_element(By.LINK_TEXT, "Logout").click()

    def view_groups(self):
        self.wd.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, group):
        self.wd.find_element(By.NAME, "new").click()
        self.wd.find_element(By.NAME, "group_name").send_keys(group.name)
        self.wd.find_element(By.NAME, "group_header").send_keys(group.header)
        self.wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        self.wd.find_element(By.NAME, "submit").click()

    def test_add_group(self):
        self.go_to_page("http://localhost/addressbook/")
        self.login("admin", "secret")
        self.view_groups()
        self.create_group(Group("qwer", "qwer", "qwer"))
        self.view_groups()
        self.logout()

    def test_add_empty_group(self):
        self.go_to_page("http://localhost/addressbook/")
        self.login("admin", "secret")
        self.view_groups()
        self.create_group(Group("", "", ""))
        self.view_groups()
        self.logout()

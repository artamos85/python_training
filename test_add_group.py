from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from group import Group
from contact import Contact


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

    def create_contact(self, contact):
        self.wd.find_element(By.LINK_TEXT, "add new").click()
        for key, value in vars(contact).items():
            if value:
                self.wd.find_element(By.NAME, key).send_keys(value)
        self.wd.find_element(By.NAME, "submit").click()

    def test_add_group(self):
        group = Group("qwer", "qwer", "qwer")
        self.go_to_page("http://localhost/addressbook/")
        self.login("admin", "secret")
        self.view_groups()
        self.create_group(group)
        self.view_groups()
        self.logout()

    def test_add_empty_group(self):
        self.go_to_page("http://localhost/addressbook/")
        self.login("admin", "secret")
        self.view_groups()
        self.create_group(Group("", "", ""))
        self.view_groups()
        self.logout()

    def test_add_contact(self):
        contact = Contact(firstname=1, middlename=2, lastname=3, nickname=4, title=6, company=7, address=8, home_phone=9, work_phone=10, mobile=8999999999, fax=11, email=12, email2=13, email3=14, homepage=15, bday=16, bmonth=17, byear=18, aday=19, amonth=20, ayear=21, address2=22, phone2=23, notes='wheepeee!')
        self.go_to_page("http://localhost/addressbook/")
        self.login("admin", "secret")
        self.create_contact(contact)

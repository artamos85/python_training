from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def view_groups(self):
        app = self.app
        wd = app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        self.view_groups()
        app = self.app
        wd = app.wd
        wd.find_element(By.NAME, "new").click()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def delete_first(self):
        self.view_groups()
        app = self.app
        wd = app.wd
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()

    def edit_first(self, group):
        self.view_groups()
        app = self.app
        wd = app.wd
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.NAME, "edit").click()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        app = self.app
        wd = app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

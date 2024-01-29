import pytest
from fixture.application import Application
from model.group import Group
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    group = Group("qwer", "qwer", "qwer")
    app.session.login("admin", "secret")
    app.group.create(group)
    app.session.logout()


def test_add_empty_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()


def test_add_contact(app):
    contact = Contact(firstname=1, middlename=2, lastname=3,
                      nickname=4, title=6, company=7, address=8,
                      home_phone=9, work_phone=10, mobile=8999999999,
                      fax=11, email=12, email2=13, email3=14,
                      homepage=15, bday=16, bmonth=17, byear=18,
                      aday=19, amonth=20, ayear=21, address2=22,
                      phone2=23, notes='wheepeee!')
    app.session.login("admin", "secret")
    app.contact.create(contact)
    app.session.logout()

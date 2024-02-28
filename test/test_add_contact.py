from model.contact import Contact


def test_add_contact(app):
    contact = Contact(firstname=1, middlename=2, lastname=3,
                      nickname=4, title=6, company=7, address=8,
                      home_phone=9, work_phone=10, mobile=8999999999,
                      fax=11, email=12, email2=13, email3=14,
                      homepage=15, bday=16, bmonth=17, byear=18,
                      aday=19, amonth=20, ayear=21, address2=22,
                      phone2=23, notes='wheepeee!')
    app.session.login('admin', 'secret')
    app.contact.create(contact)
    app.session.logout()

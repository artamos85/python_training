from model.contact import Contact


def test_edit_first_contact(app):
    contact = Contact(firstname='new1', middlename='new2', lastname='new3',
                      nickname='new4', title='new6', company='new7', address='new8',
                      home_phone='new9', work_phone='new10', mobile='+8999999999',
                      fax='new11', email='new12', email2='new13', email3='new14',
                      homepage='new15', bday='new16', bmonth='new17', byear='new18',
                      aday='new19', amonth='new20', ayear='new21', address2='new22',
                      phone2='new23', notes='wheepeee!wheepeee!')
    app.session.login("admin", "secret")
    app.contact.edit_first(contact)
    app.session.logout()
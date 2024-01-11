class Contact:
    def __init__(
            self, firstname, middlename = None,
            lastname = None, nickname = None, photo = None,
            title = None, company = None, address = None,
            home_phone = None, work_phone = None, mobile = None, fax = None,
            email = None, email2 = None, email3 = None,
            homepage = None, bday = None, bmonth = None, byear = None,
            aday = None, amonth = None, ayear = None,
            address2 = None, phone2 = None, notes = None):
        self.byear = byear
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.home = home_phone
        self.work = work_phone
        self.mobile = mobile
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes

contact = Contact(firstname=1, middlename=2, lastname=3, nickname=4, title=6, company=7)
for key, value in vars(contact).items():
    print(key, value)
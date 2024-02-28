from model.group import Group


def test_add_group(app):
    group = Group("qwer", "qwer", "qwer")
    app.session.login("admin", "secret")
    app.group.create(group)
    app.session.logout()


def test_add_empty_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()

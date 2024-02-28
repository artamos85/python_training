from model.group import Group

def test_edit_group(app):
    group = Group('rewq', 'rewq', 'rewq')
    app.session.login('admin', 'secret')
    app.group.edit_first(group)
    app.session.logout()
from DraBrIW.Storage.Database import UserDatabase


def test_init():
    db = UserDatabase("test_db")
    assert type(db) is UserDatabase



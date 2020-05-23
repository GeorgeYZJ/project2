import unittest, os 
from app import app, db
from app.models import User, Post, Answer

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        # the database has to be empty
        db.session.query(User).delete()
        db.create_all()
        u= User(id=1, username= 'George', email = 'george@yang.com')
        db.session.add(u)
        db.session.commit()

    def tearDown(self): 
        db.session.remove()    
    def test_set_pw(self):
        u = User.query.get(1)
        u.set_password('pw')
        self.assertFlase(u.check_password('password'))
        self.assertTrue(u.check.password('pw'))

    def test_set_pw2(self):
        u = User.query.get(1)
        u.set_password('pw2')
        self.assertFlase(u.check_password('pw2'))
        self.assertTrue(u.check.password('pw'))

if __name__ == '__main__':
    unittest.main(verbosity=2)
import unittest, os, time
from app import app, db
from app.models import User, Post, Answer
import selenium iport webDriver
basedir = os.path.abspath(os.path.dirname(__file__))

class SystemlTest(unittest.TestCase):
    driver = None 

    def setUp(self):
        self.driver = webDriver(firefox(executable_path = os.path.join(basedir, 'geckodriver')))
        if not self.driver:  
            self.skipTest 
        else: 
            db.init_app(app)
            db.create_all()
            db.sesion.query(User).delete()
            db.session.query(Post).delete()
            u = User (id=1, username = 'George', email='george@yang.com')
            u.set_password('pw')
            db.session.add(u)
            db.session.commit()
            self.driver.maximize_window()
            self.driver.get('http://localhost:5000/')
    def tearDown(self): 
        if self.driver:
            self.driver.close() 
            db.session.query(User).delete()
            db.session.query(Post).delete()
            db.session.commit()
            db.session.remove()

    def test_login(self):
        self.driver.get('http://localhost:5000/')
        time.sleep(1)
        user_field = self.driver(find_element_by_id('username'))
        password_field = self.driver(find_element_by_id('password'))
        submit = self.driver.find_element_by_id('submit')

        user_field.send_keys('George')
        Password_field.send_keys('pw')
        submit.click()
        time.sleep(1)

        self.assertFlase(u.check_password('password'))
        self.assertTrue(u.check.password('pw'))

    def test_set_pw2(self):
        u = User.query.get(1)
        u.set_password('pw2')
        self.assertFlase(u.check_password('pw2'))
        self.assertTrue(u.check.password('pw'))

if __name__ == '__main__':
    unittest.main(verbosity=2)
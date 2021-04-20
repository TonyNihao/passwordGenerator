import unittest
import app as backend


class unitTests(unittest.TestCase):

    def setUp(self):
        backend.app.config['TESTING'] = True
        self.backend = backend.app.test_client()

    def test_pwdGeneration(self):
        pwd = self.backend.get("/&length=50&symbols=true&uppercase=true&digits=true")
        assert pwd.status_code == 200
        assert str(pwd.data).isascii()

if __name__ == '__main__':
    unittest.main()

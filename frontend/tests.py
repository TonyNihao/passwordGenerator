import unittest
from app import app as frontend

class tests(unittest.TestCase):

    def setUp(self):
        frontend.app.config['TESTING'] = True
        self.frontend = frontend.app.test_client()

    def test_frontend(self):
        page = self.frontend.get("/")
        assert page.status_code == "200"
        assert "password".lower() in str(page.data)



if __name__ == '__main__':
    unittest.main()

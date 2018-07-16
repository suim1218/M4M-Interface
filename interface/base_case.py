import requests
import unittest


class BaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.session = requests.Session()
        url = 'http://localhost:9090/m4m/action/userAction/adminLogin'

        payload = {'account': '', 'pwd': '', 'captcha': ''}
        cls.session.post(url, payload)

    @classmethod
    def tearDownClass(cls):
        print('run after')

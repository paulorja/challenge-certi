import unittest
import requests


class HttpServerTests(unittest.TestCase):

    def test_server_must_be_running(self):
        resp = requests.get("http://localhost:8080/1", headers={'Content-Type': 'application/json'})
        print("hello")


if __name__ == '__main__':
    unittest.main()

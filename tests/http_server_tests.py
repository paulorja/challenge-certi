import unittest

class TestHttpServer(unittest.TestCase):

    def test_should_server_offline(self):
        self.assertEqual(1, 2)
        print("hello")

if __name__ == '__main__':
    unittest.main()

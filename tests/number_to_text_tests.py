import unittest

from lib import number_to_text


class NumberToTextTests(unittest.TestCase):

    def test_should_convert_1_to_text(self):
        result = "dois"
        self.assertEqual(result, "um")


if __name__ == '__main__':
    unittest.main()


import unittest

from number_to_text import NumberToText


class NumberToTextTests(unittest.TestCase):

    def test_should_return_none_when_number_is_float(self):
        parser = NumberToText()
        result = parser.number_to_text(1.5)
        self.assertEqual(result, None)

    def test_should_return_none_when_number_is_higher(self):
        parser = NumberToText()
        result = parser.number_to_text(100000)
        self.assertEqual(result, None)

    def test_should_return_none_when_number_is_smaller(self):
        parser = NumberToText()
        result = parser.number_to_text(-100000)
        self.assertEqual(result, None)

    def test_should_convert_0_to_text(self):
        parser = NumberToText()
        result = parser.number_to_text(0)
        self.assertEqual(result, "zero")

    def test_should_convert_1_to_text(self):
        parser = NumberToText()
        result = parser.number_to_text(1)
        self.assertEqual(result, "um")


if __name__ == '__main__':
    unittest.main()


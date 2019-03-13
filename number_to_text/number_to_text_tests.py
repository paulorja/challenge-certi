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

    def test_should_convert_1_negative_to_text(self):
        parser = NumberToText()
        result = parser.number_to_text(-1)
        self.assertEqual(result, "menos um")

    def test_should_convert_21_to_text(self):
        parser = NumberToText()
        result = parser.number_to_text(21)
        self.assertEqual(result, "vinte e um")

    def test_should_convert_99999_to_text(self):
        parser = NumberToText()
        result = parser.number_to_text(99999)
        self.assertEqual(result, "noventa e nove mil e novecentos e noventa e nove")

    def test_should_convert_54327_to_text(self):
        parser = NumberToText()
        result = parser.number_to_text(54327)
        self.assertEqual(result, "cinquenta e quatro mil e trezentos e vinte e sete")

    def test_should_convert_110_to_text(self):
        parser = NumberToText()
        result = parser.number_to_text(110)
        self.assertEqual(result, "cento e dez")

    def test_should_convert_70007_negative_to_text(self):
        parser = NumberToText()
        result = parser.number_to_text(-70007)
        self.assertEqual(result, "menos setenta mil e sete")

    def test_should_convert_68154_negative_to_text(self):
        parser = NumberToText()
        result = parser.number_to_text(68154)
        self.assertEqual(result, "sessenta e oito mil e cento e cinquenta e quatro")

    def test_should_convert_100_to_text(self):
        parser = NumberToText()
        result = parser.number_to_text(100)
        self.assertEqual(result, "cem")

    def test_should_convert_5100_to_text(self):
        parser = NumberToText()
        result = parser.number_to_text(5100)
        self.assertEqual(result, "cinco mil e cem")

    def test_should_convert_5113_to_text(self):
        parser = NumberToText()
        result = parser.number_to_text(5113)
        self.assertEqual(result, "cinco mil e cento e treze")

    def test_should_convert_80019_negative_to_text(self):
        parser = NumberToText()
        result = parser.number_to_text(-80019)
        self.assertEqual(result, "menos oitenta mil e dezenove")

    def test_should_convert_40201_to_text(self):
        parser = NumberToText()
        result = parser.number_to_text(40201)
        self.assertEqual(result, "quarenta mil e duzentos e um")


if __name__ == '__main__':
    unittest.main()

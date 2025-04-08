import unittest     

def roman_to_decimal(roman):
    valores = {
        'I': 1,
        'V': 5
    }

    resultado = 0
    i = 0

    while i < len(roman):
        # Si esta letra y la siguiente forman un patrón de resta (como IV o IX)
        if i + 1 < len(roman) and valores[roman[i]] < valores[roman[i + 1]]:
            resultado += valores[roman[i + 1]] - valores[roman[i]]
            i += 2  # Saltamos ambas letras
        else:
            resultado += valores[roman[i]]
            i += 1

    return resultado

class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        decimal = roman_to_decimal('I')
        self.assertEqual(decimal, 1)

    def test_II(self):
        decimal = roman_to_decimal('II')
        self.assertEqual(decimal, 2)

    def test_III(self):
        decimal = roman_to_decimal('III')
        self.assertEqual(decimal, 3)

    def test_V(self):
        decimal = roman_to_decimal('V')
        self.assertEqual(decimal, 5)

    def test_VI(self):
        decimal = roman_to_decimal('VI')
        self.assertEqual(decimal, 6)

    def test_VIII(self):
        decimal = roman_to_decimal('VIII')
        self.assertEqual(decimal, 8)

    def test_IV(self):
        decimal = roman_to_decimal('IV')
        self.assertEqual(decimal, 4)

    def test_IX(self):
        decimal = roman_to_decimal('IX')
        self.assertEqual(decimal, 9)

def main():
    my_roman = input('decime tu romano: ')
    decimal_humano = roman_to_decimal(my_roman)
    print(my_roman + ' -> ' + str(decimal_humano))

if __name__ == '__main__':
    # main()
    unittest.main()

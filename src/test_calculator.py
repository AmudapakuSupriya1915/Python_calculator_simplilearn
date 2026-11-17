import unittest

from calculator import calculator


class TestCalculator(unittest.TestCase):
	def test_add(self):
		self.assertEqual(calculator("add", 3, 2), 5)

	def test_subtract(self):
		self.assertEqual(calculator("subtract", 3, 2), 1)

	def test_invalid_operation(self):
		with self.assertRaises(ValueError):
			calculator("multiply", 3, 2)


if __name__ == "__main__":
	unittest.main()

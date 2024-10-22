import unittest
import sqlite3
from main import factorial, connect_and_store_result

class TestFactorialFunction(unittest.TestCase):
    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_of_positive_number(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_of_large_number(self):
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_of_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_database_insertion(self):
        number = 5
        result = factorial(number)
        connect_and_store_result(number, result)

        # Verify that the data was inserted correctly
        conn = sqlite3.connect('factorials.db')
        cursor = conn.cursor()
        cursor.execute('SELECT result FROM factorials WHERE number=?', (number,))
        data = cursor.fetchone()
        self.assertEqual(data[0], result)

if __name__ == "__main__":
    unittest.main()

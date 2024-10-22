"""
This module contains functions to calculate the factorial of a number
and store the result in an SQLite database.
"""

import sqlite3

def factorial(number):
    """
    Calculate the factorial of a non-negative integer `number`.
    Raise a ValueError if `number` is negative.
    """
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if number == 0 or number == 1:
        return 1
    factorial_result = 1
    for i in range(2, number + 1):
        factorial_result *= i
    return factorial_result


def connect_and_store_result(number, factorial_result):
    """
    Connect to SQLite database and store the factorial result.
    """
    conn = sqlite3.connect('factorials.db')
    cursor = conn.cursor()
    # Create table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS factorials (
        number INTEGER PRIMARY KEY,
        result INTEGER
    )''')

    # Insert factorial result into table
    cursor.execute('INSERT OR REPLACE INTO factorials (number, result) VALUES (?, ?)', (number, factorial_result))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    try:
        NUMBER = 5  # Renamed to UPPER_CASE to follow constant naming convention
        FACTORIAL_RESULT = factorial(NUMBER)  # Renamed variable to avoid redefinition
        print(f"The factorial of {NUMBER} is {FACTORIAL_RESULT}")

        # Store result in database
        connect_and_store_result(NUMBER, FACTORIAL_RESULT)
    except ValueError as e:
        print(e)


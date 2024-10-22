import sqlite3

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    Raise a ValueError if n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def connect_and_store_result(n, result):
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
    cursor.execute('INSERT OR REPLACE INTO factorials (number, result) VALUES (?, ?)', (n, result))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    try:
        number = 5
        result = factorial(number)
        print(f"The factorial of {number} is {result}")
        
        # Store result in database
        connect_and_store_result(number, result)
    except ValueError as e:
        print(e)

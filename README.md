# IDS706_Package_a_Python_Script_into_a_Command-Line_Tool

This is a repository for the assignment: IDS706_Package_a_Python_Script_into_a_Command-Line_Tool

![CI](https://github.com/therealzella/IDS706-python-github-template/actions/workflows/ci.yml/badge.svg)

## Factorial Calculator Tool

This Python tool calculates the factorial of a non-negative integer and stores the result in an SQLite database. 
It can be used to compute the factorial of any given number and save the result for future reference.

## Installation

To install the tool, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/factorial-calculator.git
   cd factorial-calculator
   
2. Install the required dependencies:
   pip install -r requirements.txt

3. Install the package locally using `setuptools`:
   python setup.py install

The tool is now installed and ready to use.

## Usage

Once installed, the tool can calculate a number's factorial and store it in an SQLite database.

### Command Line Usage:
You can run the tool directly from the command line like this:
```bash
python main.py
```
ex: The factorial of 5 is 120

## Explanation and Documentation

The tool consists of the following key functions:

- `factorial(number)`: This function calculates the factorial of a non-negative integer `number`. It raises a `ValueError` for negative inputs.
- `connect_and_store_result(number, result)`: This function connects to the SQLite database `factorials.db` and stores the calculated factorial of the input `number` along with its result.

### Files:
- `main.py`: Contains the logic for calculating the factorial and storing it in the database.
- `setup.py`: Defines the package metadata and dependencies for installation.
- `requirements.txt`: Lists the required dependencies (e.g., SQLite, pytest).

### Database:
The tool uses an SQLite database to store the computed factorials. Each result is stored with the corresponding number as the primary key.

## Running Tests

Unit tests for the tool are included in `test.py`. You can run the tests using `pytest`:

```bash
pytest
```
## Continuous Integration

This repository includes a CI/CD pipeline configured using GitHub Actions. It runs linting checks (with `pylint` and `flake8`), formatting checks (with `black`), and unit tests (with `pytest`) on every push and pull request.



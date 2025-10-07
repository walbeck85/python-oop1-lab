# Object Oriented Programming Lab - Bookstore

## Description

This lab focuses on applying object-oriented programming concepts by building two classes to model a bookstore scenario: a `Book` class and a `Coffee` class. You will implement attributes and methods that represent real-world behaviors, such as turning a book page and tipping for coffee, while practicing test-driven development.

## Table of Contents

- [Installation](#installation)  
- [Usage](#usage)  
- [Class Design](#class-design)  
- [Development Process](#development-process)  
- [Best Practices](#best-practices)  

## Installation

1. **Fork and Clone**  
   - Fork the [GitHub repository](https://github.com/walbeck85/python-oop1-lab) to your account.  
   - Clone your forked repository to your local machine.

2. **Setup Environment**  
   - Open the project in VSCode or your preferred IDE.  
   - Run `pipenv install` to install dependencies.  
   - Enter the virtual environment with `pipenv shell`.

## Usage

- Write your code in the `lib/book.py` and `lib/coffee.py` files.  
- Run tests to guide your development and verify functionality.  
- To run all tests:  
  ```bash
  pytest
  ```  
- To run tests for the `Book` class only:  
  ```bash
  pytest -x testing/book_test.py
  ```  
- To run tests for the `Coffee` class only:  
  ```bash
  pytest -x testing/coffee_test.py
  ```  
- The `-x` flag stops tests on the first failure, which is useful for test-driven development.

## Class Design

### Book

- **Attributes:**  
  - `title` (string, required)  
  - `page_count` (integer, required)

- **Methods:**  
  - `turn_page()` — prints a message indicating the page is being turned.

- **Validations:**  
  - Ensure `page_count` is an integer; otherwise, print an error message.

### Coffee

- **Attributes:**  
  - `size` (string, required; must be "Small", "Medium", or "Large")  
  - `price` (numeric, required)

- **Methods:**  
  - `tip()` — prints a tipping message and increases the price by 1.

- **Validations:**  
  - Ensure `size` is one of the accepted values; otherwise, print an error message.

## Development Process

- Create a feature branch before starting your work.  
- Use test-driven development: write tests, implement code, and refine until all tests pass.  
- Implement the `Book` class first, then the `Coffee` class.  
- Push your feature branch and open a pull request.  
- After review, merge to the `main` branch.

## Best Practices

- Add comments to explain the purpose and logic of your code.  
- Keep your README up-to-date with clear instructions and descriptions.  
- Remove any unnecessary or commented-out code before submission.  
- Clean up stale branches on GitHub after merging.  
- Ensure sensitive data is excluded from version control via `.gitignore`.

# SauceDemo Selenium Automation Tests

## Project Overview

This project contains automated UI tests for
https://www.saucedemo.com/ using Python, Selenium WebDriver,
and pytest.

## Test Scenarios

### Test 1: Login with Valid Credentials
- Open the SauceDemo website.
- Enter valid credentials.
- Verify that login succeeds.
- Verify that the Products page is displayed.

### Test 2: Add Item to Cart and Complete Checkout
- Log in as a standard user.
- Add Sauce Labs Backpack to the cart.
- Verify the cart item count.
- Open the cart and verify the product.
- Proceed to checkout.
- Enter customer information.
- Complete checkout.
- Verify the order confirmation message.

### Test 3: Locked-Out User Login
- Attempt login using the locked-out user.
- Verify the expected error message.
- Verify that login is unsuccessful.

## Prerequisites
- Python 3.10 or newer
- Google Chrome
- Git
- Internet connection

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run All Tests

```bash
python -m pytest tests/test_saucedemo_flows.py -v
```

## Run an Individual Test

Valid login:

```bash
python -m pytest tests/test_saucedemo_flows.py::test_login_with_valid_credentials -v
```

Checkout:

```bash
python -m pytest tests/test_saucedemo_flows.py::test_add_item_to_cart_and_complete_checkout -v
```

Locked-out login:

```bash
python -m pytest tests/test_saucedemo_flows.py::test_locked_out_user_sees_error_message -v
```

## Demo Credentials

Standard username: standard_user

Locked-out username: locked_out_user

Password: secret_sauce

These are public demo credentials provided for the SauceDemo website.

## Project Structure

```text
saucedemo-selenium-tests/
├── tests/
│   └── test_saucedemo_flows.py
├── requirements.txt
├── README.md
└── .gitignore
```

## GitHub Submission

Create a repository on GitHub, then run the following commands
from the project directory:

```bash
git init
git add .
git commit -m "Add SauceDemo Selenium automation tests"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/saucedemo-selenium-tests.git
git push -u origin main
```

Replace YOUR_USERNAME with your GitHub username.

## Notes
- Tests run against a live demo website.
- Checkout is simulated; no real payment is made.
- Each test uses a fresh browser session.
- Browser tests must be executed to confirm the actual results.

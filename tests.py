from myfile import add_numbers

# Adds two numbers together and expects the correct result.
def test_add_numbers_pass():
    assert add_numbers(10, 20) == 30

# Adds two numbers together and expects an INCORRECT result.
# This test intentionally fails, to test automated testing.
def test_add_numbers_fail():
    assert add_numbers(10, 20) == 25  # Incorrect expected result -- should be 30.

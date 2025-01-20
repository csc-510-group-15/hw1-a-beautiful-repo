from myfile import add_numbers

def test_add_numbers_pass():
    # This test will pass
    assert add_numbers(10, 20) == 30

def test_add_numbers_fail():
    # This test will fail intentionally
    assert add_numbers(10, 20) == 25  # Incorrect expected result

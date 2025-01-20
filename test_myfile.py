from myfile import add_numbers

def test_add_numbers_pass():
    # This test will pass
    assert add_numbers(10, 20) == 30

def test_add_numbers_fail():
    # This test will fail intentionally
    # Temporarily correcting this test to verify if autotest badge changes to "Success"
    assert add_numbers(10, 20) == 30
    # assert add_numbers(10, 20) == 25  # Incorrect expected result

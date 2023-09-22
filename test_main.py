"""
Test goes here

"""
from main import positive_real_number


def test_positive_real_number():
    # Test with a positive number
    result = positive_real_number(5)
    assert result, "Test failed for the positive number"


if __name__ == "__main__":
    test_positive_real_number()

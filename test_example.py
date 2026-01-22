"""
Simple test file for the test repository.
"""


def test_basic():
    """Basic test that always passes."""
    assert True


def test_addition():
    """Test basic addition."""
    assert 1 + 1 == 2


def test_string():
    """Test string operations."""
    assert "test".upper() == "TEST"


if __name__ == "__main__":
    print("Running tests...")
    test_basic()
    print("✓ test_basic passed")
    test_addition()
    print("✓ test_addition passed")
    test_string()
    print("✓ test_string passed")
    print("\nAll tests passed!")

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
    tests = [
        ("test_basic", test_basic),
        ("test_addition", test_addition),
        ("test_string", test_string),
    ]
    
    failed = []
    for name, test_func in tests:
        try:
            test_func()
            print(f"✓ {name} passed")
        except AssertionError as e:
            print(f"✗ {name} failed: {e}")
            failed.append(name)
        except Exception as e:
            print(f"✗ {name} error: {e}")
            failed.append(name)
    
    print()
    if failed:
        print(f"Failed tests: {', '.join(failed)}")
        exit(1)
    else:
        print("All tests passed!")
        exit(0)

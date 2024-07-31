import pytest
from Exercise import number_of_lines

@pytest.mark.parametrize("filename,expected_lines", [
    ("test.txt", 3),
    ("example.txt", 9)
])
def test_number_of_lines(filename, expected_lines):
    assert number_of_lines(filename) == expected_lines, f"Failed to count lines in {filename}"
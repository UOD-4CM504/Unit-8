import pytest
import os
from Exercise import write_nums

def test_write_nums():
    n = 10
    write_nums(n)

    assert os.path.isfile("nums.txt"), "File nums.txt does not exist..."

    with open("nums.txt", "r") as f:
        lines = f.readlines()

    expected_output = [f"{x}\n" for x in range(1, n+1)]

    assert lines == expected_output, "Output in nums.txt is not correct"
import pytest
from Exercise import load_grid, max_num_in_rows, max_num_adv

@pytest.fixture
def grid_3_by_3():
    return load_grid("grid_3_by_3.txt")

@pytest.fixture
def grid_5_by_5():
    return load_grid("grid_5_by_5.txt")

def test_max_num_adv_3_by_3(grid_3_by_3):
    assert max_num_adv(grid_3_by_3, 2) == 95
    assert max_num_adv(grid_3_by_3, 3) == 954

def test_max_num_in_rows_3_by_3(grid_3_by_3):
    assert max_num_in_rows(grid_3_by_3, 2) == 94
    assert max_num_in_rows(grid_3_by_3, 3) == 945

def test_max_num_in_rows_5_by_5(grid_5_by_5):
    assert max_num_in_rows(grid_5_by_5, 2) == 91
    assert max_num_in_rows(grid_5_by_5, 3) == 912
    assert max_num_in_rows(grid_5_by_5, 4) == 9123

def test_max_num_adv_5_by_5(grid_5_by_5):
    assert max_num_adv(grid_5_by_5, 2) == 97
    assert max_num_adv(grid_5_by_5, 3) == 971
    assert max_num_adv(grid_5_by_5, 4) == 9127
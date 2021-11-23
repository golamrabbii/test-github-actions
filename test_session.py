import pytest
from session import add_numbers

def test_positive_numbers():
    assert add_numbers(2,2) == 4

def test_add_zero():
    assert add_numbers(1,0) == 1
    
def test_add_negative():
    assert add_numbers(4,-100) == -96
    
def test_check_error():
    with pytest.raises(TypeError):
        add_numbers(4,'hello') 
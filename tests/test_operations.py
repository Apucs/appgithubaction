from src.math_operations import add, sub, mul

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0

def test_sub():
    assert sub(5,3)==2
    assert sub(4,3)==1
    assert sub(3,3)==0
    assert sub(2,3)==-1

def test_mul():
    assert mul(5,3)==15
    assert mul(4,3)==12
    assert mul(3,0)==0
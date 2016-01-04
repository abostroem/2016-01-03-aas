'''
Functions to do simple arithmetic
'''
def add_three(a, b, c):
    '''Adds three numbers, returns sum'''
    return a+b+c
def test_add_three():
    '''Test case for add three functions with 1,1,1'''
    assert(add_three(1,1,1)==3)

def subtract_two_from_one(a, b, c):
    '''Subtract c and a from b'''
    return a-b-c

def test_subtract_two_from_one():
    '''test case for subtract_two_from_one with 3, 2, 1'''
    assert(subtract_two_from_one(3, 1, 2) == 1)


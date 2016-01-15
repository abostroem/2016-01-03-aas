'''Here are functions to raise single numbers to powers'''

import sys

def pow3(base):
    '''raise to the third power'''
    return base**3

def pow4(base):
    '''raise to the fourth power'''
    return base**4

def test_pow3():
    try:
        assert(pow3(4) == 64)
        print('test_pow3 successful')
    except AssertionError:
        print('test_pow3 unsuccessful')
        sys.exit(1)

if __name__ == "__main__":
    '''Run the following lines if executing make_power.py as a script'''
    test_pow3()
    print(pow3(4))
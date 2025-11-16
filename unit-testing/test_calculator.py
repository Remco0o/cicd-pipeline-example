#-----------------------------------------------------------

import pytest
import os
import sys

#-----------------------------------------------------------

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

#-----------------------------------------------------------

from calc.calculator import Calculator

#-----------------------------------------------------------

@pytest.fixture
def calculator():

    return Calculator()

#-----------------------------------------------------------

def test_zero(calculator):

    assert calculator.square_root(0) == pytest.approx(expected=0.0, rel=1e-6)

#-----------------------------------------------------------

def test_positive_number(calculator):

    assert calculator.square_root(25) == pytest.approx(expected=5.0, rel=1e-6)

#-----------------------------------------------------------

def test_negative_number(calculator):

    with pytest.raises(ValueError):
        
        calculator.square_root(-10)

#-----------------------------------------------------------

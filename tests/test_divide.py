import pytest
from app.plugins.divide import DivideCommand

def test_divide_command():
    command = DivideCommand()
    # Test a regular division
    assert command.execute(10, 2) == 5

def test_divide_by_zero():
    command = DivideCommand()
    # Test division by zero, which should raise a ValueError
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        command.execute(10, 0)
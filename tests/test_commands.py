import pytest
from app.commands.commands import Command

def test_command_execute_abstract():
    with pytest.raises(TypeError):
        Command()

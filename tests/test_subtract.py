from app.plugins.subtract import SubtractCommand

def test_subtract_command():
    command = SubtractCommand()
    assert command.execute(10, 3) == 7
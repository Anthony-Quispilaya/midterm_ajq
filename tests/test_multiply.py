from app.plugins.multiply import MultiplyCommand

def test_multiply_command():
    command = MultiplyCommand()
    assert command.execute(4, 2) == 8
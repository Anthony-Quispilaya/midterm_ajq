from app.plugins.add import AddCommand

def test_add_command():
    command = AddCommand()
    assert command.execute(5, 3) == 8
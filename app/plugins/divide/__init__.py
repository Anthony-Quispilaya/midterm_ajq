from app.commands.commands import Command

class DivideCommand(Command):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

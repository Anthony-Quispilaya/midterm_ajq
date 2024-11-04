from app.commands.commands import Command

class AddCommand(Command):
    def execute(self, a, b):
        return a + b
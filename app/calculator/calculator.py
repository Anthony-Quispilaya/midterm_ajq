from app.plugins.plugin_manager import PluginManager

class Calculator:
    def __init__(self):
        self.plugin_manager = PluginManager()

    def run(self):
        while True:
            try:
                # Prompt for the command name
                command_name = input("Enter command 'exit' or 'quit' to quit: ").strip().lower()
                
                if command_name in ['exit', 'quit']:
                    print("Terminating...")
                    break

                # Check if the command is valid
                if command_name not in self.plugin_manager.commands:
                    print("Unknown command. Please try again.")
                    continue

                # Prompt for the two numbers separately
                try:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
                    continue

                # Execute the command
                result = self.plugin_manager.execute(command_name, [num1, num2])
                print(f"The answer is: {result}")
            except Exception as e:
                print(f"Error: {e}")

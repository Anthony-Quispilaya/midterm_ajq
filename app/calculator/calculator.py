from app.plugins.plugin_manager import PluginManager
from app.history_manager import HistoryManager
class Calculator:
    def __init__(self):
        self.plugin_manager = PluginManager()
        self.history_manager = HistoryManager()

    def run(self):
        try:
            while True:
                # Prompt for the command name
                command_name = input("Enter command 'exit' or 'quit' to quit: ").strip().lower()
                
                if command_name in ['exit', 'quit']:
                    print("Terminating...")
                    break
                    
                # Prompt for history command
                if command_name == "history":
                    self.history_manager.show_history()
                    continue

                # Check if the command is valid
                if command_name not in self.plugin_manager.commands:
                    print("Unknown command. Please try again.")
                    continue

                # Prompt for the two numbers separately
                try:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                    result = self.plugin_manager.execute(command_name, [num1, num2])
                    print(f"The answer is: {result}")
                    # Adds record to history
                    self.history_manager.add_record(command_name, num1, num2, result)
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
                except Exception as e:
                    print(f"Error: {e}")
        finally:
            self.history_manager.clear_temp_file()

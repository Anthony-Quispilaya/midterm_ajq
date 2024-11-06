from app.plugins.plugin_manager import PluginManager
from app.history_manager import HistoryManager
import logging

class Calculator:
    def __init__(self):
        self.plugin_manager = PluginManager()
        self.history_manager = HistoryManager()

    def run(self):
        try:
            while True:
                command_name = input("Enter command (e.g., add, subtract, history) or 'exit' to quit: ").strip().lower()
                
                if command_name in ['exit', 'quit']:
                    logging.info("Calculator Application Exiting")
                    print("Terminating...")
                    break

                if command_name == "history":
                    logging.info("Displaying calculation history")
                    self.history_manager.show_history()
                    continue

                if command_name not in self.plugin_manager.commands:
                    logging.warning(f"Unknown command '{command_name}' entered")
                    print("Unknown command. Please try again.")
                    continue

                try:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                    result = self.plugin_manager.execute(command_name, [num1, num2])
                    print(f"The answer is: {result}")
                    self.history_manager.add_record(command_name, num1, num2, result)
                except ValueError:
                    logging.error("Invalid input: Non-numeric value entered.")
                    print("Invalid input. Please enter numeric values.")
                except Exception as e:
                    logging.error(f"An error occurred: {e}")
        finally:
            self.history_manager.clear_temp_file()
            logging.info("Application cleanup complete. Exiting.")

import pandas as pd
import os

class HistoryManager:
    def __init__(self, file_path="temp_history.csv"):
        self.file_path = file_path
        # Load history from file or initialize an empty DataFrame
        if os.path.exists(self.file_path):
            self.history = pd.read_csv(self.file_path)
        else:
            self.history = pd.DataFrame(columns=["Operation", "Operand1", "Operand2", "Result"])

    def add_record(self, operation, operand1, operand2, result):
        """Add a calculation record to the history and save it to the file."""
        new_record = {"Operation": operation, "Operand1": operand1, "Operand2": operand2, "Result": result}
        self.history = self.history.append(new_record, ignore_index=True)
        # Save the history to the CSV file each time a new record is added
        self.history.to_csv(self.file_path, index=False)

    def show_history(self):
        """Display the current calculation history."""
        if self.history.empty:
            print("No calculation history available.")
        else:
            print(self.history)

    def clear_temp_file(self):
        """Delete the temporary CSV file on exit."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            print("Temporary history file deleted.")

import pandas as pd
import os
import logging

class HistoryManager:
    def __init__(self, file_path="temp_history.csv"):
        self.file_path = file_path
        logging.debug(f"Initializing HistoryManager with file '{file_path}'")
        if os.path.exists(self.file_path):
            self.history = pd.read_csv(self.file_path)
            logging.info("Loaded existing history file.")
        else:
            self.history = pd.DataFrame(columns=["Operation", "Operand1", "Operand2", "Result"])
            logging.info("No history file found. Initialized empty history.")

    def add_record(self, operation, operand1, operand2, result):
        new_record = pd.DataFrame([{
            "Operation": operation, 
            "Operand1": operand1, 
            "Operand2": operand2, 
            "Result": result
        }])
        self.history = pd.concat([self.history, new_record], ignore_index=True)
        self.history.to_csv(self.file_path, index=False)
        logging.debug(f"Added record: {operation}({operand1}, {operand2}) = {result}")

    def show_history(self):
        if self.history.empty:
            logging.info("Displayed empty history")
            print("No calculation history available.")
        else:
            print(self.history)
            logging.info("Displayed history records")

    def clear_temp_file(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            logging.info("Temporary history file deleted.")

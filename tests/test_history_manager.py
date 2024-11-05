import pytest
import os
import pandas as pd
from app.history_manager import HistoryManager

@pytest.fixture
def history_manager():
    # Create a HistoryManager with a temporary file path
    manager = HistoryManager(file_path="test_history.csv")
    yield manager
    # Teardown: remove the test file after testing
    if os.path.exists("test_history.csv"):
        os.remove("test_history.csv")

def test_initialization_no_file(history_manager):
    # Ensure an empty DataFrame is created if the file does not exist
    assert history_manager.history.empty
    assert os.path.exists("test_history.csv") == False

def test_initialization_with_file(history_manager):
    # Create a CSV file to simulate existing history
    df = pd.DataFrame([{"Operation": "add", "Operand1": 5, "Operand2": 10, "Result": 15}])
    df.to_csv("test_history.csv", index=False)
    # Re-initialize the HistoryManager to load from the file
    history_manager = HistoryManager(file_path="test_history.csv")
    assert not history_manager.history.empty
    assert history_manager.history.iloc[0]["Result"] == 15

def test_add_record(history_manager):
    history_manager.add_record("multiply", 3, 4, 12)
    # Check that the record was added to the DataFrame
    assert len(history_manager.history) == 1
    assert history_manager.history.iloc[0]["Result"] == 12
    # Check that the record was saved to the CSV file
    saved_history = pd.read_csv("test_history.csv")
    assert len(saved_history) == 1
    assert saved_history.iloc[0]["Result"] == 12

def test_show_history_empty(capsys, history_manager):
    # Test output when history is empty
    history_manager.show_history()
    captured = capsys.readouterr()
    assert "No calculation history available." in captured.out

def test_show_history_with_data(capsys, history_manager):
    # Add a record and test output when history has data
    history_manager.add_record("add", 5, 10, 15)
    history_manager.show_history()
    captured = capsys.readouterr()
    assert "add" in captured.out
    assert "5" in captured.out  # Check without decimal places
    assert "10" in captured.out  # Check without decimal places
    assert "15" in captured.out  # Check without decimal places

def test_clear_temp_file(history_manager):
    # Create a file and ensure it exists, then delete it
    history_manager.add_record("subtract", 8, 3, 5)
    assert os.path.exists("test_history.csv")
    history_manager.clear_temp_file()
    assert not os.path.exists("test_history.csv")
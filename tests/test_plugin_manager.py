import pytest
from app.plugins.plugin_manager import PluginManager

@pytest.fixture
def plugin_manager():
    # Create a PluginManager instance for testing
    return PluginManager()

def test_plugin_manager_loads_plugins(plugin_manager):
    # Ensure plugins are loaded by checking for expected commands
    assert "add" in plugin_manager.commands
    assert "subtract" in plugin_manager.commands
    assert "multiply" in plugin_manager.commands
    assert "divide" in plugin_manager.commands

def test_plugin_manager_execute_add(plugin_manager):
    # Test addition command
    result = plugin_manager.execute("add", [5, 3])
    assert result == 8

def test_plugin_manager_execute_subtract(plugin_manager):
    # Test subtraction command
    result = plugin_manager.execute("subtract", [10, 3])
    assert result == 7

def test_plugin_manager_execute_multiply(plugin_manager):
    # Test multiplication command
    result = plugin_manager.execute("multiply", [4, 2])
    assert result == 8

def test_plugin_manager_execute_divide(plugin_manager):
    # Test division command
    result = plugin_manager.execute("divide", [10, 2])
    assert result == 5

def test_plugin_manager_execute_divide_by_zero(plugin_manager):
    # Test division by zero, which should raise a ValueError
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        plugin_manager.execute("divide", [10, 0])

def test_plugin_manager_invalid_command(plugin_manager):
    # Test executing an invalid command, which should raise a ValueError
    with pytest.raises(ValueError, match="Unknown command: invalid"):
        plugin_manager.execute("invalid", [1, 2])

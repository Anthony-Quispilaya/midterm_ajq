import pkgutil
import importlib
import logging
from app.commands.commands import Command

class PluginManager:
    def __init__(self, plugins_package="app.plugins"):
        self.commands = {}
        self.plugins_package = plugins_package
        logging.debug(f"Initializing PluginManager with package '{plugins_package}'")
        self.load_plugins()

    def load_plugins(self):
        for _, plugin_name, _ in pkgutil.iter_modules([self.plugins_package.replace('.', '/')]):
            try:
                plugin_module = importlib.import_module(f"{self.plugins_package}.{plugin_name}")
                self.register_plugin(plugin_name, plugin_module)
                logging.info(f"Loaded plugin: {plugin_name}")
            except ImportError as e:
                logging.error(f"Error loading plugin {plugin_name}: {e}")

    def register_plugin(self, plugin_name, plugin_module):
        for attr_name in dir(plugin_module):
            attr = getattr(plugin_module, attr_name)
            if isinstance(attr, type) and issubclass(attr, Command) and attr is not Command:
                self.commands[plugin_name] = attr()
                logging.debug(f"Registered command '{plugin_name}'")

    def execute(self, command_name, args):
        if command_name in self.commands:
            logging.debug(f"Executing command '{command_name}' with args {args}")
            return self.commands[command_name].execute(*args)
        else:
            logging.warning(f"Attempted to execute unknown command '{command_name}'")
            raise ValueError(f"Unknown command: {command_name}")

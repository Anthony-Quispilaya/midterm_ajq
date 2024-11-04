# apps/plugins/plugin_manager.py
import os
import importlib

class PluginManager:
    def __init__(self):
        self.plugins = {}
        self.load_plugins()

    def load_plugins(self):
        plugins_dir = os.path.dirname(__file__)
        for foldername in os.listdir(plugins_dir):
            folder_path = os.path.join(plugins_dir, foldername)
            if os.path.isdir(folder_path) and foldername not in ['__pycache__', 'plugin_manager']:
                module_name = f"app.plugins.{foldername}"
                try:
                    module = importlib.import_module(module_name)
                    if hasattr(module, 'command_name') and hasattr(module, 'run'):
                        self.plugins[module.command_name] = module.run
                except ModuleNotFoundError:
                    print(f"Could not load plugin: {module_name}")

    def execute(self, command_name, args):
        if command_name in self.plugins:
            return self.plugins[command_name](args)
        else:
            raise ValueError(f"Unknown command: {command_name}")

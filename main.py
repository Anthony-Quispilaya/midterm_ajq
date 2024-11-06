from app.calculator.calculator import Calculator
import logging
import logging.config
import os

# Set up logging configuration
if os.path.exists("logging.conf"):
    logging.config.fileConfig("logging.conf")
else:
    logging.basicConfig(level=logging.INFO)

# Now import the rest of the application after configuring logging
from app.calculator.calculator import Calculator

if __name__ == "__main__":
    logging.info("Starting Calculator Application")
    calculator = Calculator()
    calculator.run()
    logging.info("Calculator Application Stopped")

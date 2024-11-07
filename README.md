# Calculator Application

This application is an interactive, command-line calculator that uses a Read-Eval-Print Loop (REPL) interface. It enables users to enter commands interactively and receive immediate results for arithmetic operations, history viewing, and other functionalities.


## Features

REPL Interface: The REPL interface allows users to interactively enter commands like add, subtract, multiply, and divide, followed by two numbers. The application instantly evaluates the input and returns results in real-time.

Plugin Architecture: Each operation (addition, subtraction, multiplication, division) is a standalone plugin, making it easy to extend the application with additional commands.

History Management: Tracks each calculation performed during a session and enables users to view the history.

Error Handling: Handles invalid inputs and division by zero with clear error messages.

Logging: Logs events such as command executions, errors, and user interactions for better debugging and monitoring.


### This application relies on the following libraries:

pytest: For automated testing and ensuring code reliability.

pytest-cov: Adds code coverage measurement to pytest to ensure that tests cover all parts of the application.

Faker: Generates random test data, allowing robust testing with diverse inputs.

pandas: Manages the calculation history by storing, displaying, and saving data in a structured format.

logging: Standard Python library used for logging application events, making it easier to trace and debug the program.


## Commands in REPL Interface

After running main.py, the REPL interface will prompt for commands. Here are some commands you can enter:

Addition: add - Prompts for two numbers and returns their sum.

Subtraction: subtract - Prompts for two numbers and returns their difference.

Multiplication: multiply - Prompts for two numbers and returns their product.

Division: divide - Prompts for two numbers and returns their quotient. Handles division by zero with an error message.

View History: history - Displays all previous calculations for the session.

Exit: exit - Ends the REPL session and exits the program.


## Acknowledgements

This application was built using Python 3.10, with libraries such as pytest, Faker, and pandas.

### Submission:
https://youtu.be/Ux8BM--n53k?feature=shared

import os
from app.calculator.calculator import Calculator

def main():
    print("Welcome to the calculator")
    calculator = Calculator()
    calculator.run()
    
if __name__ == "__main__":
    os.system('clear')
    main()
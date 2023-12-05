# The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment.
#  It allows operating on the interpreter as it provides access to the variables and functions that interact strongly with the interpret

# Here's what each part of the code is doing:

# 1. **`error_message_detail` function:**
#    - This function takes two parameters, `error` and `error_detail`.
#    - It extracts information from the `error_detail` about where the error occurred in the Python script.
#    - It constructs a human-readable error message with details such as the script name, line number, and the actual error message.
#    - The constructed error message is then returned.

# 2. **`CustomException` class:**
#    - This is a custom exception class that inherits from the built-in `Exception` class.
#    - It has an `__init__` method that takes `error_message` and `error_detail` as parameters.
#    - The `super().__init__(error_message)` line calls the constructor of the parent `Exception` class with the provided error message.
#    - It then initializes its own `error_message` attribute by calling the `error_message_detail` function with the provided error message and error details.
#    - The `__str__` method is overridden to return the custom error message when the exception is converted to a string (e.g., when printing the exception).

# In simple terms, this code is creating a custom exception class called `CustomException`. When an instance of this exception is raised,
#  it captures details about where the error occurred in the script and constructs a more informative error message. 
#  This can be useful for debugging and providing meaningful error information when an exception is caught.

import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1 / 0  # This triggers a ZeroDivisionError
    except ZeroDivisionError:
        logging.info("Divide by zero: This is a user-friendly message.")
    except CustomException as ce:
        logging.error(ce)  # Log the CustomException without re-raising
    except Exception as e:
        logging.error("An unexpected error occurred: {}".format(e))

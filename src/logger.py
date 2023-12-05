# Logging is a means of tracking events that happen when some software runs.

# This code sets up logging for a Python script or application. Logging is a way to capture and record information about the execution of your code, 
# which can be useful for debugging, monitoring, or understanding how your program behaves over time.

# Here's what each part of the code is doing:

# 1. **Setting up the log file:**
#    - `LOG_FILE`: Generates a unique log file name based on the current date and time.
#    - `logs_path`: Constructs a path to the directory where log files will be stored.
#    - `os.makedirs(logs_path, exist_ok=True)`: Creates the directory specified by `logs_path` if it doesn't exist.

# 2. **Configuring logging:**
#    - `LOG_FILE_PATH`: Specifies the full path to the log file.
#    - `logging.basicConfig`: Configures the logging system with the following settings:
#      - `filename`: Sets the log file where the log messages will be written.
#      - `format`: Defines the structure of each log message, including the timestamp, line number, logger name, log level, and the actual log message.
#      - `level`: Sets the minimum log level to be recorded. In this case, it's set to `logging.INFO`,
#      which means only messages at the INFO level and above will be recorded.

# In simple terms, this code creates a log file with a unique name based on the current date and time. 
# It configures the logging system to write log messages to this file with a specific format. This way, when you run your Python script or application, 
# it will generate a log file in the specified directory, capturing information about the program's execution.


import logging
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m_%d%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)


LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)


logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s -%(levelname)s -%(message)s",
    level = logging.INFO,


)

if __name__ == "__main__":
    logging.info("Logging has started")
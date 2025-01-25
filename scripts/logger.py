import logging
import logging.config
import os
import json

# Get the root directory dynamically
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
LOGS_DIR = os.path.join(ROOT_DIR, "logs")

def setup_logger():
    # Ensure the logs directory exists
    if not os.path.exists(LOGS_DIR):
        os.makedirs(LOGS_DIR)

    # Path to the log config JSON file
    log_config_path = os.path.join(LOGS_DIR, "log_config.json")
    if not os.path.exists(log_config_path):
        raise FileNotFoundError(f"Log config file not found: {log_config_path}")

    # Load and configure the logging
    with open(log_config_path, "r") as file:
        config = json.load(file)

    # Dynamically update the file handler path
    config["handlers"]["file_handler"]["filename"] = os.path.join(LOGS_DIR, "app.log")
    logging.config.dictConfig(config)

def get_logger(name):
    if not logging.getLogger().handlers:  # Check if logging is already configured
        setup_logger()
    return logging.getLogger(name)

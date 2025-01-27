# This script is used to load environment variables from the .env file.


import os
import logger

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(path, '.env')
logger = logger.get_logger(__name__)

def load_env():
    if os.path.exists(env_path):

        try:
            with open(env_path , 'r') as file:
                for line in file:
                    if not line.startswith('#'):
                        key, value = line.strip().split('===')
                        os.environ[key] = value
                logger.info("Environment variables loaded successfully")
        except Exception as e:
            logger.error(f"Error loading environment variables {e}")
    else:
        logger.error("Environment file not found")

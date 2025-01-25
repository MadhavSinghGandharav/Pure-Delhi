# setup file to setup the basic project structure to work on
'''if this script doesn't work then you need to setup the project structure manually

   // STEPS TO SETUP PROJECT STRUCTURE MANUALLY //

   1. Make Sure you have python insatlled on your system and added to PATH
   2. Run the following commands in the terminal
        python -m pip install --upgrade pip
        python -m pip install virtualenv

   3. Open your terminal and navigate to the Project Directory (Pure-Delhi)
   4. Run the following commands in the terminal
        python -m venv venv
        source venv/bin/activate       ( for linux or mac )
        venv\\Scripts\\activate          ( for windows )
        pip install -r Requirements.txt

   '''

   # import the required modules
import os
import platform
from logger import get_logger
import subprocess

class Setup:
    def __init__(self):
        self.logger = get_logger(__name__)
        self.path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.venv_path = os.path.join(self.path, 'venv')
        self.requirments_path = os.path.join(self.path, 'Requirements.txt')
        self.platform = platform.system()


    def command(self,cmd):
        try:
            subprocess.run(cmd, check=True, shell=True,stdout=subprocess.DEVNULL, )
            self.logger.info(f"Command succeeded: {cmd}")
            return True

        except subprocess.CalledProcessError as e:
            self.logger.error(f"Command failed: {e.stderr}")
            return False

    def create_virtual_envirnonment(self):
        if os.path.exists(self.venv_path):
            self.logger.info("Virtual Environment already exists")
            print("Virtual Environment already exists")
            return True

        print("Creating Virtual Environment")
        self.logger.info("Creating Virtual Environment")
        commands = [
            "python -m pip install --upgrade pip",
            "python -m pip install virtualenv",
            f"python -m venv {self.venv_path}"
        ]

        for cmd in commands:
            if not self.command(cmd):
                return False
        self.logger.info("Virtual Environment Created Successfully")

    def install_requirements(self):
        if not os.path.exists(self.requirments_path):
            self.logger.error("Requirements file not found")
            print("Requirements file not found")
            return False

        print("Installing Requirements")
        self.logger.info("Installing Requirements")

        if self.platform == 'Windows':
            cmd = f"{os.path.join(self.venv_path, 'Scripts', 'activate')} && pip install -r {self.requirments_path}"
        else:
            cmd = f"source {os.path.join(self.venv_path, 'bin', 'activate')} && pip install -r {self.requirments_path}"

        return self.command(cmd)

    def print_instructions(self):
           """Print activation instructions"""
           print("\nProject Setup Completed Successfully :-)")
           print("To activate the virtual environment navigate to project root directory (Pure-Delhi) and, run:")
           if platform.system() == 'Windows':
               print("venv\\Scripts\\activate")
           else:
               print("source venv/bin/activate")

    def run(self):
        try:
            if not self.create_virtual_envirnonment():
                raise Exception("Failed to setup virtual environment")

            if not self.install_requirements():
                raise Exception("Failed to install requirements")

            self.print_instructions()
            self.logger.info('Project Setup Completed Successfully')
            return True

        except Exception as e:
            self.logger.error(f'Project Setup Failed: {str(e)}')
            print(f"Error: {str(e)}")
            return False

if __name__ == "__main__":
    setup = Setup()
    setup.run()

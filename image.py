import subprocess
import sys

def create_executable(script_path):
    # Ensure PyInstaller is installed
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

    # Create a single executable file
    subprocess.check_call(["pyinstaller", "--onefile", script_path])

if __name__ == "__main__":
    create_executable("image_resizer.py")

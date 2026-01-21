import pathlib
import sys

def save_data_to_yaml(data, currentProjectPath):
    print(f"data type: {type(data)}")
    print(f"currentProjectPath type: {type(currentProjectPath)}")
    # This line triggers the error if currentProjectPath is a dict
    project_path = pathlib.Path(currentProjectPath)
    print(f"Path created: {project_path}")

data_dict = {"nodes": {}}
path_str = "/tmp/project"

print("Attempting to call save_data_to_yaml with swapped arguments (path, data)...")
try:
    # Simulating the call in app.py: save_data_to_yaml(self.appData.currentProjectPath, data)
    # where first arg is path (str) and second is data (dict)
    save_data_to_yaml(path_str, data_dict)
except TypeError as e:
    print(f"\nCaught expected TypeError: {e}")
except Exception as e:
    print(f"\nCaught unexpected exception: {type(e).__name__}: {e}")

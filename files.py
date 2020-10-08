import os
from Overlord import config_reader

config = config_reader()
files = config["FILES"]
test_path = files["Path"]

def name_manipulator(old_str, new_str):
    """
    Replaces parts of names
    example: name_manipulator("serhio", "kopo")
    """
    for root, dirs, files in os.walk(test_path):
        for name in files:
            new_name = name.replace(old_str, new_str)
            os.rename(os.path.join(root, name), os.path.join(root, new_name))
            print(f"{name} changed to {new_name}")

def dir_info():
    """
    Returns number of files in directory
    """
    number_of_files = len([files for root, dirs, files in os.walk(test_path) for name in files if os.path.isfile(os.path.join(root, name))])
    print(f"There are {number_of_files} files in {test_path}")
    return number_of_files
    
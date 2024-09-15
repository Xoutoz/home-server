import os


def find_compose_yaml_paths(root_directory):
    # List to store paths of directories containing 'compose.yaml'
    compose_yaml_paths = []

    # Walk through the directory
    for dirpath, dirnames, filenames in os.walk(root_directory):
        # Check if 'compose.yaml' is in the current directory
        if 'compose.yaml' in filenames:
            # If found, append the directory path to the list
            compose_yaml_paths.append(dirpath)

    return compose_yaml_paths


def create_directories_in_home(directories):
    # Get the user's home directory
    home_directory = os.path.expanduser("~")

    for directory in directories:
        # Construct the full path for the new directory
        new_directory_path = os.path.join(home_directory, directory.split("/")[-1])

        try:
            # Create the directory (if it doesn't exist)
            os.makedirs(new_directory_path, exist_ok=True)
            print(f"Directory created: {new_directory_path}")

        except Exception as e:
            print(f"Error creating directory {new_directory_path}: {e}")

# Define the root directory (current working directory in this case)
root_directory = os.getcwd()

# Get the list of paths containing 'compose.yaml'
paths_with_compose_yaml = find_compose_yaml_paths(root_directory)

# Reorder app paths
apps = [ path for path in paths_with_compose_yaml ]
apps.append(apps.pop(apps.index(f"{root_directory}/reverse-proxy")))
create_directories_in_home(apps)
import os
import subprocess


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

# Define the root directory (current working directory in this case)
root_directory = os.getcwd()

# Get the list of paths containing 'compose.yaml'
paths_with_compose_yaml = find_compose_yaml_paths(root_directory)

# Reorder app paths
apps = [ path for path in paths_with_compose_yaml ]
apps.append(apps.pop(apps.index(f"{root_directory}/reverse-proxy")))

def launch_docker_compose_services(services):
    for service in services:
        try:
            # Construct the command to stop the service
            command = ['docker', 'compose', '-f', f'{service}/compose.yaml', 'up', '-d']

            # Run the command
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Print the output for logging/debugging purposes
            print(f"Successfully started service: {service}", result.stdout.decode())

        except subprocess.CalledProcessError as e:
            # Handle errors during the subprocess execution
            print(f"Error stopping service: {service}")
            print(e.stderr.decode())

        except Exception as ex:
            # Handle other exceptions
            print(f"An unexpected error occurred: {ex}")

launch_docker_compose_services(apps)

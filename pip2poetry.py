import argparse
import subprocess
import os

def convert_requirements_to_poetry(requirements_file, project_name="my_project"):
    # Create a new directory for the project
    if not os.path.exists(project_name):
        os.makedirs(project_name)

    # Initialize pyproject.toml using poetry
    subprocess.run(['poetry', 'new', '--name', project_name, project_name], check=True)
    
    # Read requirements.txt and add each dependency
    with open(requirements_file, 'r') as file:
        dependencies = file.readlines()
    
    # Change directory to the newly created project
    os.chdir(project_name)

    for dependency in dependencies:
        dependency = dependency.strip()
        if dependency and not dependency.startswith('#'):
            # Add each dependency to pyproject.toml using poetry
            subprocess.run(['poetry', 'add', dependency], check=True)
    
    # Install dependencies to generate poetry.lock
    subprocess.run(['poetry', 'install'], check=True)

    print(f"Converted {requirements_file} to pyproject.toml and poetry.lock in {project_name}/ directory")

# Example usage


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--requirements", required=True, type=str)
    parser.add_argument("-p", "--poetry-lock", required=True, type=str)
    return parser.parse_args()

if __name__ == "__main__":

    args = parse_args()

    
    convert_requirements_to_poetry(args.requirements, args.poetry_lock)


#  All the packages is here that required for Ml

from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str):
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and req.strip() != HYPEN_E_DOT]

    return requirements

setup(
    name='ML_project',
    version='0.0.1',
    author='jangidapeksha',
    author_email='jangidapeksha918@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    dependency_links=['-e .'],
)



# **`setup.py`:**
# - This file is used to configure how your Python project should be installed and what its properties are.

# Here's what each part of the code is doing:

# 1. **`get_requirements` function:**
#    - This function reads the contents of the `requirements.txt` file and extracts the list of requirements.
#    - It removes any empty lines and excludes the special `-e .` line from the list.

# 2. **`setup` function:**
#    - Configures the metadata for your project (name, version, author, etc.).
#    - Uses `find_packages()` to automatically discover and include all Python packages in your project.
#    - Calls the `get_requirements` function to get the list of dependencies from `requirements.txt` (excluding `-e .`).
#    - Sets up the installation requirements using the obtained list.
#    - Includes `dependency_links=['-e .']` to specify that the local project (indicated by `-e .` in `requirements.txt`) should be installed in editable mode.

# In simple terms, the code is setting up the information needed to install your Python project.
# It reads the dependencies from `requirements.txt` (excluding the special `-e .` line),
# and it specifies that your project should be installed in editable mode when using this list of dependencies.
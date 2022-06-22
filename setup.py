from gettext import find
from setuptools import setup , find_packages
from typing import List

# Declaring variables for setup
NAME = "Housing Prediction Project"
VERSION = "0.0.1"
AUTHOR = "Sayon Bhattacharjee"
DESCRIPTION = "First Project"
REQUIREMENTS_FILE_NAME = "requirements.txt"

# To install libraries from requirements file
def get_requirements_list()->List[str]:
    
    """
    This function will return all the libraries present
    in requirements.txt file as list.
    Returns List of libraries.
    """

    with open(REQUIREMENTS_FILE_NAME) as file:
        return file.readlines().remove("-e .")

setup(
    name = NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = find_packages(), # our custom packages in housing folder
    install_requires = get_requirements_list() # external packages from requirements.txt file
)
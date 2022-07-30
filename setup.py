from setuptools import setup,find_packages
from typing import List

# Declaring variables for setup functions

PROJECT_NAME = "Housing-Predictor"
VERSION = "0.0.1"
AUTHOR = "Aakash Pal"
DESCRIPTION = "This is a first FSDS Nov Batch Machine Learning Project"
PACKAGES = ["Housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description : This function is going to return list of requirement mention in requirements.txt

    return This function is going to return a list which contain name of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirements_file:
        return requirements_file.readlines().remove("-e .")


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()
)
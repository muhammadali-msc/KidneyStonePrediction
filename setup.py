from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:

    requriements = []
    
    with open(file_path) as file_obj:

        requriements = file_obj.readlines()
        requriements = [req.replace('\n', "") for req in requriements]

        if HYPEN_E_DOT in requriements:
            requriements.remove(HYPEN_E_DOT)

        return requriements

setup(
    name = "KindeyStonePrediction",
    version = "0.0.2",
    author = "Muhammad Ali",
    author_email = "muhammadalimsc21@gmail.com",
    packages = find_packages(),
    install_requries = get_requirements("requirements.txt")
)
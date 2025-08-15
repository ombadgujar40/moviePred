from setuptools import find_packages, setup
from typing import List

def get_requirenments(file_path:str) -> List[str]:
    requirenments = []
    HYPHEN_DOT = "-e ."
    with open(file_path) as file_obj:
        requirenments = file_obj.readlines()
        requirenments = [req.replace("\n", " ") for req in requirenments]
        if HYPHEN_DOT in requirenments:
            requirenments.remove(HYPHEN_DOT)
            
    return requirenments

setup(
    name="Ml Generic",
    version="0.0.0.1",
    author="any",
    packages=find_packages(),
    install_requirenments = get_requirenments("requirenments.txt")
)
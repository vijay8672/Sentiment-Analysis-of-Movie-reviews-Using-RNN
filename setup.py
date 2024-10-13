from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path: str)->list:
  "this function will return the list of requirements"

  requirements=[]
  with open(file_path) as file_obj:
    requirements=file_obj.readlines()
    requirements= [req.replace('\n', ' ') for req in requirements]

    if HYPEN_E_DOT in requirements:
      requirements.remove(HYPEN_E_DOT)

  return requirements


setup(
    name='Sentiment Analysis using Recurrent Neural Network',                       # project name
    version='0.1',                                                                  # Version of the package
    author='Vijay Kumar Kodam',                                                     # Author name
    author_email='vijay.kodam98@gmail.com',                                               # Your email
    description='A deep learning project for sentiment analysis of movie reviews',  # Short description of Project
    packages=find_packages(),                                                       # Automatically find packages in the project
    install_requires=get_requirements('requirements.txt')                           # Listing out the packages/libraries
)

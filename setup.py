from setuptools import setup, find_packages

HYPHEN_E_DOT = "-e ."

def get_requirements(filepath:str):
    '''
    Read requirements from a file
    '''
    requirements = []
    with open(filepath, "r") as f:
        requirements = f.read().splitlines()

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
name='Text-Summariser',
version='0.0.1',
author='finn1010',
author_email='finniankane@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)
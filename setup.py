from setuptools import setup, find_packages

HYPEN_E_DOT = "-e ."
def get_requirements(filename):
    with open(filename) as f:
        requirements = f.read().splitlines()
    requirements = [r for r in requirements if r != HYPEN_E_DOT]
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='John',
    author_email='phanqu6ctoan@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
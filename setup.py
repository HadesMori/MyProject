from setuptools import setup, find_packages

setup(
    name="MyProject",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pytest>=7.0.0",
        "flake8>=6.0.0",
        "black>=23.0.0",
    ],
)
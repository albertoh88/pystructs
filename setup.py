from setuptools import setup, find_packages

setup(
    name="pystructs",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    description="Functional utilities for nested data structures and validations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="albertoh88",
    license="MIT",
    python_requires=">=3.8,<3.13"
)
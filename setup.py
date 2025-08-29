from setuptools import setup, find_packages
from pathlib import Path

# Lee README.md con codificación UTF-8
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="pystructs-utils",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    description="Functional utilities for nested data structures and validations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="albertoh88",
    license="MIT",
    python_requires=">=3.8"
)
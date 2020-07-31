from setuptools import setup, find_packages
from os.path import join, dirname

with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name='argparse_dataclasses',
    version='0.1',
    packages=find_packages(),
    author="Felix Neko",
    author_email="felix-neko@list.ru",
    long_description = long_description,
    long_description_content_type = "text/markdown",
)
# pylint: skip-file
"""To build python wheel run:
   python setup.py sdist bdist_wheel
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="template",
    version="1.0.0",
    author="kwhytee",
    description="template package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kwhytee/python-template",
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3", "Operating System :: OS Independent"],
)

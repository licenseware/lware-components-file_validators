from setuptools import setup, find_packages

#Distribute py wheels
#python3 setup.py bdist_wheel sdist
#twine check dist/*
#cd dist 
#twine upload *

with open("README.md", "r") as fh:
    long_description = fh.read()


setup (
	name="file_validators",
	version="0.0.1",
	description="Validate contents from excel, csv's and txt files",
	url="https://github.com/licenseware/lware-components-file_validators",
	author="licenseware",
	author_email="contact@licenseware.io",
	license='',
	py_modules=["file_validators"],
	install_requires=['pandas', 'openpyxl'],
	packages=find_packages(exclude=("tests","files_test",)),
	long_description=long_description,
    long_description_content_type="text/markdown",
	package_dir={"":"src"}
)
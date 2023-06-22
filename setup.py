from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in employee_report/__init__.py
from employee_report import __version__ as version

setup(
	name="employee_report",
	version=version,
	description="Employee Detail Report",
	author="Peniel Technology LLC",
	author_email="jyoti@penieltech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

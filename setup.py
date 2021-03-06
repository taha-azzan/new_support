# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in new_support/__init__.py
from new_support import __version__ as version

setup(
	name='new_support',
	version=version,
	description='Maintenace App',
	author='Partner Team',
	author_email='t.azzan@partner-cons.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

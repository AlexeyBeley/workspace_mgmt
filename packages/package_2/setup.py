import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "dome9", "common"))
#print(os.listdir(sys.path[0]))
print(sys.path)
from sample_package import __version__

from setuptools import setup, find_packages

def readme():
	with open('README.md') as f:
		return f.read()


setup(
	name='dome9.common.sample_package',
	version=__version__,
	description='Dome9 sample common package',
	long_description=readme(),
	author='Dome9 devops sre team',
	author_email='d9ops@checkpoint.com',
	license='MIT',
	packages=["dome9.common.sample_package"],
	include_package_data=True,
	install_requires=[],
	zip_safe=False)

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "horey", "common"))

from package_1 import __version__

from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='horey.common.package_1',
      version=__version__,
      description='Horey package_1',
      long_description=readme(),
      author='Horey',
      author_email='alexey.beley@gmail.com',
      license='MIT',
      packages=["horey.common.package_1"],
      include_package_data=True,
      install_requires=[],
      zip_safe=False)

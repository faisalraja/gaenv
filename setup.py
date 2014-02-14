#! /usr/bin/env python
from setuptools import setup, find_packages
import sys
import os

version = '0.1.7'


def main():
    setup(name='gaenv',
          version=version,
          description="Tool to manage packages for google app engine",
          long_description=open('README.rst').read(),
          classifiers=[
              'Development Status :: 3 - Alpha',
              'Environment :: Console',
              'Intended Audience :: Developers',
              'Programming Language :: Python',
              'License :: OSI Approved :: MIT License'
          ],
          keywords='google app engine environment tool',
          author='Faisal Raja',
          author_email='support@altlimit.com',
          url='http://github.com/faisalraja/gaenv',
          license='MIT',
          packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
          include_package_data=True,
          zip_safe=False,
          install_requires=['setuptools'],
          entry_points={
              "console_scripts": ['gaenv = gaenv:main'],
          },
          )


if __name__ == '__main__':
    main()

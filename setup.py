#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''The setup script.'''

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'yacponf',
]

test_requirements = [
    'pytest',
    'pytest-runner',
    'tox',
]

setup(
    name='toy_package',
    version='0.0.1',
    description='An example package',
    long_description=readme,
    author='Logan Asher Jones',
    author_email='me@loganasherjones.com',
    url='https://github.com/loganasherjones/toy_package',
    packages=find_packages(include=['toy_package']),
    include_package_data=True,
    install_requires=requirements,
    license='MIT license',
    zip_safe=False,
    keywords='logan',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)

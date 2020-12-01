#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]


setup(
    author="A Student",
    author_email='student@example.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Tulane NLP project",
    entry_points={
        'console_scripts': [
            'nlp=nlp.cli:main',
            'stats=nlp.cli:stats',
            'train=nlp.cli:train',
            'web=nlp.cli:web',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='nlp',
    name='nlp',
    packages=find_packages(include=['nlp', 'nlp.app', 'nlp.app.templates', 'nlp.app.static']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/tulane-cmps6730/sample-project',
    version='0.1.0',
    zip_safe=False,
)

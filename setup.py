#!/usr/bin/env python3
"""
Setup script for Video Translator application
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='video-translator-en-to-bn',
    version='1.0.0',
    description='A free desktop application that translates video audio from English to Bengali',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Infinity-Programmer',
    url='https://github.com/yourusername/video-translator',
    py_modules=['video_translator', 'example_usage'],
    install_requires=requirements,
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia :: Video',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    keywords='video translator english bengali speech-recognition text-to-speech',
    entry_points={
        'console_scripts': [
            'video-translator=video_translator:main',
        ],
    },
)

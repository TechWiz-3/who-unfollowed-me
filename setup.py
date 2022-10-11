from setuptools import setup, find_packages
from os import path

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

# Get the long description from the README file
with open("README.md", encoding="utf-8") as f:
    read_file = f.read()
 

setup(
    name="unfollow",
    url="https://github.com/TechWiz-3/who-unfollowed-me",
    author="Zac the Wise aka TechWiz-3",
    version='2.0.0',
    description="😡 Python CLI tool that shows you who has unfollowed you on GitHub",
    packages=['unfollow'],
    long_description=read_file,
    long_description_content_type='text/markdown',
    entry_points='''
    [console_scripts]
    unfollow=unfollow.cli:main
    ''',
    classifiers=classifiers,
    install_requires=['rich'],
)
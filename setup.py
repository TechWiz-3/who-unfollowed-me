from setuptools import setup, find_namespace_packages
from pathlib import Path

#project_dir = Path(__file__).parent
#long_description = (project_dir / "README.md").read_text()

setup(
    name="unfollow",
    url="https://github.com/TechWiz-3/who-unfollowed-me",
    author="Zac the Wise aka TechWiz-3",
    version='1.0.0',
    description="😡 Python CLI tool that shows you who has unfollowed you on GitHub",
    packages=find_namespace_packages(include=['src.*']),
#    long_description_content_type='text/markdown',
#    long_description=long_description,
    scripts=["unfollow"],
    install_requires=['rich'],
)

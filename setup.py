from setuptools import setup, find_packages
from pathlib import Path

#project_dir = Path(__file__).parent
#long_description = (project_dir / "README.md").read_text()

setup(
    name="unfollow",
    url="https://github.com/TechWiz-3/who-unfollowed-me",
    author="Zac the Wise aka TechWiz-3",
    version='1.0.4',
    description="😡 Python CLI tool that shows you who has unfollowed you on GitHub",
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        unfollow=unfollow.cli:main
    ''',
#    long_description_content_type='text/markdown',
#    long_description=long_description,
    install_requires=['rich'],
)

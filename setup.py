from setuptools import setup, find_packages

setup(
    name='task_cli',
    version='0.0.1',
    description='A lightweight task manager CLI',
    author='Belam Muia',
    packages=find_packages(),
    install_requires=[
        "click",
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "tasks=task_manager.cli:cli",  
        ],
    },
)

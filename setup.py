from setuptools import setup, find_packages
with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

setup(
    name="eid",
    version="0.0.1",
    description="machine learning experiment easily in docker container",
    author="yamad07",
    packages=['eid', 'eid.lib', 'eid.lib.templates'],
    package_data={
        'eid': ['lib/templates/*']
        },
    entry_points={
        "console_scripts": [
            "eid=eid.core:main",
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ]
)

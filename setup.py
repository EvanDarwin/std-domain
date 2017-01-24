from setuptools import setup, find_packages

import sys

excluded_packages = ['build', 'dist']

setup(
    name="std-domain",
    version="0.1.0",
    author="Evan Darwin",
    author_email="github@noreply.users.github.com",
    description="Handle international domain names and punycodes easily",
    license="MIT",
    keywords="IDN punycodes international domain library",
    url="https://github.com/WhoisBuster/std-domain",
    packages=find_packages(exclude=excluded_packages),
    classifiers=[
        "License :: Other/Proprietary License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Internationalization",
        "Topic :: Software Development :: Libraries",
    ],
)

 # IntegrationAPI/setup.py

from setuptools import setup, find_packages

setup(
    name="IntegrationAPI",
    version="0.1.0",
    description="Python package for integrating with various APIs.",
    author="Sirisha Jotheeswaran Padmasekhar",
    author_email="sirishajpadmasekhar@gmail.com",
    packages=find_packages(),
    install_requires=[
        "tweepy",
        "paypalrestsdk",
        "googlemaps",
    ],
)

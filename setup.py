from setuptools import setup
import os

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as wfile:
    README = wfile.read()

setup(
    name="durationstring",
    version=__import__("durationstring").__version__,
    description="Get readable time in seconds.",
    long_description=README,
    url="https://github.com/geonyoro/durationstring",
    author="George Nyoro",
    author_email="geonyoro@gmail.com",
    license="MIT License",
    py_modules=["durationstring"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

from os.path import join, dirname
import re

from setuptools import setup, find_packages


def read(*names, **kwargs):
    with open(
        join(dirname(__file__), *names), encoding=kwargs.get("encoding", "utf8")
    ) as fh:
        return fh.read()


readme = re.compile("^.. start-badges.*^.. end-badges", re.M | re.S).sub(
    "", read("README.rst")
)
changelog = re.sub(":[a-z]+:`~?(.*?)`", r"``\1``", read("CHANGELOG.rst"))

with open("requirements.dev.txt") as f:
    dev_requirements = f.read().splitlines()

setup(
    name="vardef",
    version="0.1.0",
    packages=find_packages(
        exclude=(
            "tests",
            "examples",
            "docs",
            ".eggs",
            ".github",
            ".pytest_cache",
            ".tox",
            "build",
            "dist",
            "htmlcov",
            "vardef.egg-info",
        )
    ),
    url="https://github.com/allrod5/vardef",
    license="MIT",
    author="Rodrigo Martins de Oliveira",
    author_email="oliveira.rodrigo.m@gmail.com",
    description="Python decorator to turn a function into a variable definition",
    long_description=f"{readme}\n{changelog}",
    keywords="vardef def variable delegate delegates value definition",
    python_requires=">=3.6",
    install_requires=[],
    setup_requires=[],
    test_requires=dev_requirements,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: IronPython",
        "Programming Language :: Python :: Implementation :: Jython",
        "Programming Language :: Python :: Implementation :: MicroPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: Stackless",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Typing :: Typed",
    ],
)

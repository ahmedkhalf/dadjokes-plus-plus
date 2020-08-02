import re

from setuptools import find_packages, setup  # type: ignore

# Version info -- read without importing
with open("dadjokes/__init__.py", "rt", encoding="utf8") as f:
    version_re = re.search(r"__version__ = \"(.*?)\"", f.read())
    if version_re:
        version = version_re.group(1)
    else:
        raise ValueError("Could not determine package version")
    # Normalize version so `setup.py --version` show same version as twine.
    version = str(version)

# Add readme as long description
with open("README.md") as f:
    long_description = f.read()

# Library dependencies
INSTALL_REQUIRES = [
    "requests",
]

# Testing dependencies
TEST_REQUIRES = [
    "black",
    "flake8",
]

setup(
    name="dadjokes-plus-plus",
    version=version,
    license="MIT",
    description="Dad jokes on steroids.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    author="Ahmed Khalf",
    author_email="ahmedkhalf567@gmail.com",
    url="https://github.com/ahmedkhalf/dadjokes-plus-plus",
    download_url="https://github.com/ahmedkhalf/dadjokes-plus-plus/archive/1.0.tar.gz",
    keywords=[
        "icanhazdadjoke",
        "dadjokes",
        "cli",
        "terminal",
        "comedy",
        "jokes",
        "python",
    ],
    entry_points={"console_scripts": ["dadjokes=dadjokes.main:main"]},
    install_requires=INSTALL_REQUIRES,
    extras_require={"test": TEST_REQUIRES},
    python_requires=">=3.6",
    classifiers=[
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Terminals",
        "Topic :: Software Development",
    ],
)

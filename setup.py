import os
import sys

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))

# Check if Auto-sklearn *could* run on the given system
if os.name != "posix":
    raise ValueError(
        "Detected unsupported operating system: %s. Please check "
        "the compability information of auto-sklearn: https://automl.github.io"
        "/auto-sklearn/master/installation.html#windows-osx-compatibility"
        % sys.platform
    )

if sys.version_info < (3, 7):
    raise ValueError(
        "Unsupported Python version %d.%d.%d found. Auto-sklearn requires Python "
        "3.7 or higher."
        % (sys.version_info.major, sys.version_info.minor, sys.version_info.micro)
    )

with open(os.path.join(HERE, "requirements.txt")) as fp:
    install_reqs = [
        r.rstrip()
        for r in fp.readlines()
        if not r.startswith("#") and not r.startswith("git+")
    ]

extras_reqs = {
    "test": [
        "pytest>=4.6",
        "pytest-cov",
        "pytest-forked",
        "pytest-timeout",
        "pytest-cases>=3.6.11",
        "mypy",
        "isort",
        "black",
        "pydocstyle",
        "openml",
        "pre-commit",
    ],
    "examples": [
        "matplotlib",
        "jupyter",
        "notebook",
        "seaborn",
    ],
    "docs": [
        "sphinx<4.3",
        "sphinx-gallery",
        "sphinx_bootstrap_theme",
        "numpydoc",
        "sphinx_toolbox",
        "docutils==0.16",
    ],
}

with open(os.path.join(HERE, "autosklearn", "__version__.py")) as fh:
    version = fh.readlines()[-1].split()[-1].strip("\"'")


with open(os.path.join(HERE, "README.md")) as fh:
    long_description = fh.read()


setup(
    name="auto-sklearn",
    author="Matthias Feurer",
    author_email="feurerm@informatik.uni-freiburg.de",
    description="Automated machine learning.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=version,
    packages=find_packages(exclude=["test", "scripts", "examples"]),
    extras_require=extras_reqs,
    install_requires=install_reqs,
    include_package_data=True,
    license="BSD3",
    platforms=["Linux"],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    url="https://automl.github.io/auto-sklearn",
)

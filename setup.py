import pwnedcheck

from distutils.core import setup

setup(
    name="PwnedCheck",
    packages=["pwnedcheck"],
    package_dir={"pwnedcheck": "pwnedcheck"},
    version=pwnedcheck.__version__,
    description="Python package to interact with http://haveibeenpwned.com",
    long_description=open("README.rst").read() + "\n\n" + open("CHANGES.rst").read(),
    author="Casey Dunham",
    author_email="casey.dunham@gmail.com",
    url="https://github.com/caseydunham/PwnedCheck",
    license=open("LICENSE.rst").read(),
    classifiers=(
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Security",
    )
)
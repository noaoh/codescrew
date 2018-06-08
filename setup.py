#/usr/bin/python3
from setuptools import setup 
setup(
        name="codescrew",
        version="1.0.0",
        description="A simple utility for pulling pranks on your friend's
        code (and to undo it)",
        url="https://github.com/noaoh/codescrew",
        author="Noah Holt",
        author_email="noahryanholt@gmail.com",
        license="BSD",
        python_requires=">=3"
        keywords="pranks fun command-line unicode",
        install_requires=["argparse","re"],
        entry_points={'console_scripts": ["codescrew =\
                main:Main']}
)

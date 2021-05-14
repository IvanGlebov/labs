from setuptools import setup

import pyvcs

AUTHOR = "Ivan Glebov"
AUTHOR_EMAIL = "glebov.vanya@list.ru"
HOME_PAGE = "https://github.com/Dementiy/pybook-assignments"

setup(
    name="pyvcs",
    version=pyvcs.__version__,
    # version="1.0",
    description="The stupid content tracker",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=["pyvcs"],
    entry_points={"console_scripts": ["pyvcs = pyvcs.__main__:main"]},
    url=HOME_PAGE,
    license="GPLv3",
    python_requires=">=3.6.0",
)

mlir/utils/mbr/setup.py
=======================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    from setuptools import setup
from setuptools import find_packages


setup(
    name="mbr",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "mbr = mbr.main:main",
        ],
    },
)



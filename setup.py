from setuptools import setup

import py2exe

setup(
    windows=[{
        "script": "bmi_calculator.py",
        "icon_resources": [(1, "bmi.ico")]  # Optional icon
    }],
    options={
        "py2exe": {
            "bundle_files": 1,
            "compressed": True
        }
    },
    zipfile=None
)

"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup
from glob import glob

APP = ['pmb.py']
DATA_FILES = []
OPTIONS = {}

setup(
    app=['pmb.py'],
    data_files=['physicell_logo_200px.png',
        ('../data', glob('../data/*.xml')),
    ],
    options={'py2app': OPTIONS},
    py_modules=['config_tab','microenv_tab','cell_def_tab','user_params_tab'],
    setup_requires=['py2app'],
)
"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup
from glob import glob

APP = ['pmb.py']
DATA_FILES = []
OPTIONS = {"includes": ["PyQt5", "pandas", "matplotlib"],}


setup(
    app=['pmb.py'],
    data_files=['physicell_logo_200px.png',
        ('../data', glob('../data/*.xml')),
        ('../data', glob('../data/*.bnd')),
        ('../data', glob('../data/*.cfg')),
    ],
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],

   py_modules=['config_tab','microenv_tab','populate_tree_cell_defs','cell_def_tab','user_params_tab','ics_tab','run_tab','vis_tab','legend_tab','pyMCDS_cells'],
#    py_modules=['config_tab','microenv_tab','cell_def_tab','user_params_tab','ics_tab','run_tab','legend_tab'],
    # py_modules=['config_tab','microenv_tab','cell_def_tab','user_params_tab'],
)

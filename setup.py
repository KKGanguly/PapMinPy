from setuptools import setup, find_packages
setup(name = 'PapMinPy',
    version = '0.1a',
    description = 'a paper parsing package developed for parsing different items from academic papers in pdf',
    packages = find_packages(),
    install_requires = [
    'bs4'
    ],
)

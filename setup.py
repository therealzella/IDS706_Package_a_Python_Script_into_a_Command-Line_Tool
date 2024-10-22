from setuptools import setup, find_packages

setup(
    name="factorial_package",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'factorial-calc=main:factorial',
        ],
    },
    install_requires=[],
)

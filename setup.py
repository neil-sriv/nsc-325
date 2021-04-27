from setuptools import setup

setup(
    name='netscan',
    version='0.1',
    py_modules=['netscan'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        netscan=netscan:cli
    ''',
)
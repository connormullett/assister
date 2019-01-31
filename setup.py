
from setuptools import setup

VERSION = '0.1.0'

setup(
        name='assister',
        version=VERSION,
        packages=['assister'],
        entry_points={
            'console_scripts': [
                'assister=assister.__main__:main'
            ]
        }
    )


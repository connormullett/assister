
from setuptools import setup

setup(
        name='assister',
        version='0.2.0',
        packages=['assister'],
        entry_points={
            'console_scripts': [
                'ass=assister.__main__:main'
            ]
        }
    )


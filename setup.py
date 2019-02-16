
from setuptools import setup, find_packages

setup(
        name='cm-assister',
        author='Connor Mullett',
        version='1.0.0',
        description='Simple Assister CLI, https://github.com/connormullett/assister',
        packages=['assister', find_packages(exclude='tests')],
        include_package_data=True,
        license='MIT',
        url='https://github.com/connormullett/assister',
        entry_points={
            'console_scripts': [
                'ass=assister.__main__:main'
            ]
        }
    )


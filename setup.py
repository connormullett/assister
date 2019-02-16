
from setuptools import setup

setup(
        name='cm-assister',
        author='Connor Mullett',
        version='1.0.2',
        description='Simple Assister CLI, https://github.com/connormullett/assister',
        packages=['assister/todos', 'assister/api_requester', 'assister/dir_builder'],
        include_package_data=True,
        license='MIT',
        url='https://github.com/connormullett/assister',
        entry_points={
            'console_scripts': [
                'ass=assister.__main__:main'
            ]
        }
    )


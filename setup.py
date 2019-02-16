
from setuptools import setup

setup(
        name='assister',
        author='Connor Mullett',
        version='1.1.0',
        description='Simple Assister CLI, https://github.com/connormullett/assister',
        packages=['assister/todos', 'assister/api_requester', 'assister/dir_builder'],
        install_requires=['tqdm'],
        include_package_data=True,
        license='MIT',
        url='https://github.com/connormullett/assister',
        entry_points={
            'console_scripts': [
                'ass=assister.__main__:main'
            ]
        }
    )


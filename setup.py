import setuptools


setuptools.setup(
    name='mvg',
    version='1.0',
    author='Florian Pfisterer',
    description='Access MVG data from your command line.',
    packages=['mvgcli'],
    install_requires=[line.strip() for line in open('requirements.txt', 'r').readlines()],
    python_requires='>=3.5',
    entry_points={
        'console_scripts': ['mvg=mvgcli.cli:main']
    }
)
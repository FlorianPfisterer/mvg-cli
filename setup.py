import setuptools
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

# replace the image URL to be able to show it on PyPI
README = README.replace(
    '(./example.png)',
    '(https://github.com/FlorianPfisterer/mvg-cli/raw/main/example.png)'
)


setuptools.setup(
    name='mvg-cli',
    version='1.0.0',

    author='Florian Pfisterer',
    author_email='florian@pfisterer.dev',

    description='A CLI tool to get quick access to live MVG data from the command line.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/FlorianPfisterer/mvg-cli',

    packages=['mvgcli'],
    include_package_data=True,
    install_requires=[line.strip() for line in open('requirements.txt', 'r').readlines()],
    python_requires='>=3.5',
    entry_points={
        'console_scripts': ['mvg=mvgcli.cli:main']
    }
)
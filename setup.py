from setuptools import setup

setup(
    name='BingoCardGenerator',
    version='',
    packages=['bingocardgenerator'],
    url='http://www.github.com/JasonKessler/BingoCardGenerator',
    license='Apache 2',
    author='Jason Kessler',
    author_email='',
    install_requires=[
        'scattertext',
        'pyate',
    ],
    description='Make an HTML bingo card from free text',

)

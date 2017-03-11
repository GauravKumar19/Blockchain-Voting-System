from setuptools import setup

setup(
    name='OnlineBallotRegulator',
    version='1.0.0',
    author='Mattie432',
    author_email='matt@mattie432.com',
    description='',
    url='https://github.com/Mattie432/Blockchain-Voting-System',
    packages=[
        'onlineballotregulator',
        'database'
    ],
    install_requires=[
        'Twisted>=17.1.0',
        'psycopg2'
    ]
)

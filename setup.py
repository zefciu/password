from setuptools import setup

setup(
    name = 'password',
    version = '0.2',
    author = 'Szymon Pyżalski',
    author_email = 'zefciu <szymon@pythonista.net>',
    description = 'A password attribute that stores hashes',
    license = 'BSD',
    tests_require = ['nose>=1.0', 'nose-cov>=1.0'],
    py_modules = ['password']
)

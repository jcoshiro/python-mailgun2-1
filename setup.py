try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import mailgun2

setup(
    name=mailgun2.__title__,
    packages=[mailgun2.__title__],
    version=mailgun2.__version__,
    description='A python client for Mailgun API v2',
    author=mailgun2.__author__,
    author_email='tech@zerocater.com',
    url='https://github.com/ZeroCater/python-mailgun2',
    download_url='https://github.com/ZeroCater/python-mailgun2/archive/0.1.3.tar.gz',
    keywords=['mailgun', 'email'],
    install_requires=[
        'requests>=1.2.3',
    ],
    test_suite="tests",
    tests_require=[
        'mock>=0.8',
    ],
)

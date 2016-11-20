import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import ast
import re


def get_version():
    _version_re = re.compile(r'__version__\s+=\s+(.*)')

    with open('pageobject/__init__.py', 'rb') as f:
        version = str(ast.literal_eval(_version_re.search(
            f.read().decode('utf-8')).group(1)))

    return version


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = [
            '--strict',
            '--verbose',
            '--tb=long',
            '--cov-report',
            'term:skip-covered',
            '--cov-report',
            'term-missing',
            '--cov=pageobject',
            'tests/']

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


long_description = 'Page Object design pattern implementation' + \
       ' using selenium WebDriver'

setup_args = {
    'name': 'pageobject',
    'packages': ['pageobject'],
    'version': get_version(),
    'description': 'Page Object implementation',
    'long_description': long_description,
    'url': 'https://github.com/lukas-linhart/pageobject',
    'author': 'Lukas Linhart',
    'author_email': 'lukas.linhart.1981@gmail.com',
    'license': 'MIT',
    'classifiers': ['Development Status :: 3 - Alpha',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: MIT License',
                    'Operating System :: POSIX',
                    'Operating System :: MacOS :: MacOS X',
                    'Operating System :: Microsoft :: Windows',
                    'Topic :: Software Development :: Quality Assurance',
                    'Topic :: Software Development :: Testing',
                    'Programming Language :: Python :: 2',
                    'Programming Language :: Python :: 2.7',
                    'Programming Language :: Python :: 3',
                    'Programming Language :: Python :: 3.5'],
    'keywords': 'pageobject browser automation',
    'packages': find_packages(exclude=['contrib', 'docs', 'tests*']),
    'install_requires': ['selenium>=3.0.1'],
    'tests_require': ['pytest', 'pytest-cov'],
    'cmdclass': {'test': PyTest},
}

setup(**setup_args)


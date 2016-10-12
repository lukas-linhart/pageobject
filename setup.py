from setuptools import setup, find_packages

long_description = 'Page Object design pattern implementation' + \
       ' using selenium WebDriver'

setup_args = {
    'name': 'pageobject',
    'packages': ['pageobject'],
    'version': '0.0.9',
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
    'install_requires': ['selenium>=2.53.0']
}

setup(**setup_args)


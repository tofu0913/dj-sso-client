import os
from setuptools import setup
from djssoclient import __version__

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='dj-sso-client2',
    version=__version__,
    packages=['djssoclient',],
    include_package_data=True,
    license='GPL v2.0',
    description='A Django SSO client application, works with dj-sso-server',
    long_description=README,
    url='https://github.com/tofu0913/dj-sso-client',
    author='Fan Fei, Cliff Chen',
    author_email='tofu0913@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

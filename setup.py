# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
version = open(os.path.join(here, 'VERSION.txt')).readline().rstrip()

setup(name='repoze.what.plugins.ini',
      version=version,
      description='repoze.what pluggin with sources based on INI files.',
      long_description=README,
      classifiers=[],
      keywords='wsgi repoze what pluggins authorization INI ini',
      author='Jose Dinuncio',
      author_email='jdinunci@uc.edu.ve',
      url='http://github.com/jdinuncio/repoze.what.plugins.ini/tree/master',
      license='BSD-derived (see http://www.repoze.org/LICENSE.txt)',

      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      tests_require=['repoze.what', 'nose'],
      test_suite="nose.collector",
      install_requires=['repoze.what', 'pyparsing'],
      namespace_packages=['repoze', 'repoze.what', 'repoze.what.plugins'],
      entry_points="""\
      """,
      )

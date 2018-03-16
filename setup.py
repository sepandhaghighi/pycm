# -*- coding: utf-8 -*-
from setuptools import setup
setup(
  name = 'pycm',
  packages = ['pycm'],
  version = '0.8',
  description = 'Multiclass confusion matrix library in python',
  long_description='''
   In the field of machine learning and specifically the problem of statistical classification,
   a confusion matrix, also known as an error matrix, is a specific table layout that allows visualization of
   the performance of an algorithm, typically a supervised learning one (in unsupervised learning it is usually
   called a matching matrix). Each row of the matrix represents the instances in a predicted class while each column
   represents the instances in an actual class (or vice versa) pycm(python confusion matrix) is a multi-class
   confusion matrix library in python.''',
  author = 'Sepand Haghighi',
  author_email = 'sepand@qpage.ir',
  url = 'https://github.com/sepandhaghighi/pycm',
  download_url = 'https://github.com/sepandhaghighi/pycm/tarball/v0.8',
  keywords = "confusion-matrix python3 python machine_learning ML",
  project_urls={
    'Webpage': 'http://pycm.shaghighi.ir',
    'Source': 'https://github.com/sepandhaghighi/pycm',
     },
  install_requires=[
	  'codecov',
      'art',
      'numpy',
      ],
  python_requires='>=2.7',
  classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Natural Language :: English',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3.3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Topic :: Scientific/Engineering :: Information Analysis',
    ],
  license='MIT',
)

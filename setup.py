# -*- coding: utf-8 -*-
from setuptools import setup


def get_requires():
    requirements = open("requirements.txt", "r").read()
    return list(filter(lambda x: x != "", requirements.split()))


setup(
    name='pycm',
    packages=['pycm'],
    version='0.8.1',
    description='Multi-class confusion matrix library in Python',
    long_description='''
   PyCM is a multi-class confusion matrix library written in Python that
   supports both input data vectors and direct matrix, and a proper tool for
   post-classification model evaluation that supports most classes and overall
   statistics parameters.
   PyCM is the swiss-army knife of confusion matrices, targeted mainly at
   data scientists that need a broad array of metrics for predictive models
   and an accurate evaluation of large variety of classifiers.''',
    author='Sepand Haghighi',
    author_email='sepand@qpage.ir',
    url='https://github.com/sepandhaghighi/pycm',
    download_url='https://github.com/sepandhaghighi/pycm/tarball/v0.8.1',
    keywords="confusion-matrix python3 python machine_learning ML",
    project_urls={
        'Webpage': 'http://pycm.shaghighi.ir',
        'Source': 'https://github.com/sepandhaghighi/pycm',
    },
    install_requires=get_requires(),
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

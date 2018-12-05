# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_requires():
    requirements = open("requirements.txt", "r").read()
    return list(filter(lambda x: x != "", requirements.split()))


def read_description():
    try:
        with open("README.md") as r:
            description = "\n"
            description += r.read()
        with open("CHANGELOG.md") as c:
            description += "\n"
            description += c.read()
        return description
    except Exception:
        return '''
   PyCM is a multi-class confusion matrix library written in Python that
   supports both input data vectors and direct matrix, and a proper tool for
   post-classification model evaluation that supports most classes and overall
   statistics parameters.
   PyCM is the swiss-army knife of confusion matrices, targeted mainly at
   data scientists that need a broad array of metrics for predictive models
   and an accurate evaluation of large variety of classifiers.'''


setup(
    name='pycm',
    packages=['pycm'],
    version='1.6',
    description='Multi-class confusion matrix library in Python',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    author='Sepand Haghighi',
    author_email='sepand@qpage.ir',
    url='https://github.com/sepandhaghighi/pycm',
    download_url='https://github.com/sepandhaghighi/pycm/tarball/v1.6',
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
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    license='MIT',
)

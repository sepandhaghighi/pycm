# -*- coding: utf-8 -*-
"""Setup module."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_requires():
    """Read requirements.txt."""
    requirements = open("requirements.txt", "r").read()
    return list(filter(lambda x: x != "", requirements.split()))


def read_description():
    """Read README.md and CHANGELOG.md."""
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
    version='4.2',
    description='Multi-class confusion matrix library in Python',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    author='PyCM Development Team',
    author_email='info@pycm.io',
    url='https://github.com/sepandhaghighi/pycm',
    download_url='https://github.com/sepandhaghighi/pycm/tarball/v4.2',
    keywords="confusion-matrix python3 python machine_learning ML",
    project_urls={
        'Webpage': 'https://www.pycm.io',
        'Source': 'https://github.com/sepandhaghighi/pycm',
        'Discord': 'https://discord.com/invite/zqpU2b3J3f',
    },
    install_requires=get_requires(),
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
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

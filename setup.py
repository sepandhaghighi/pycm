from distutils.core import setup
setup(
  name = 'pycm',
  packages = ['pycm'],
  version = '0.4',
  description = 'Confusion Matrix In Python',
  long_description='Confusion Matrix In Python',
  author = 'Sepand Haghighi',
  author_email = 'sepand@qpage.ir',
  url = 'https://github.com/sepandhaghighi/pycm',
  download_url = 'https://github.com/sepandhaghighi/pycm/tarball/v0.4',
  keywords = ['confusion-matrix', 'python3','python','machine learning','ML'],
  install_requires=[
	  'codecov',
      'art',
      ],
  classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Natural Language :: English',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Topic :: Text Processing :: Fonts',
    ],
  license='MIT',
)

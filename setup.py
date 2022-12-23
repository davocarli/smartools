import os

from distutils.core import setup

def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()

setup(
  name = 'smartools',
  packages = ['smartools', 'smartools.models', 'smartools.models.enums', 'smartools.operations', 'smartools.types'],
  version = '1.2.0',
  license='MIT',
  description = 'A wrapper for the smartsheet-python-sdk that monkey-patches in new methods & functionality.',
  long_description=read_file('README.md'),
  long_description_content_type='text/markdown',
  author = 'David Carli-Arnold',
  author_email = 'davocarli@gmail.com',
  url = 'https://github.com/davocarli',
  keywords = ['Smartsheet', 'smartsheet-python-sdk', 'monkey-patch'],
  install_requires=[
          'smartsheet-python-sdk',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)

from distutils.core import setup
setup(
  name = 'smartools',
  packages = ['smartools', 'smartools.models', 'smartools.models.enums', 'smartools.operations', 'smartools.types'],
  version = '0.1.7',
  license='MIT',
  description = 'A wrapper for the smartsheet-python-sdk that monkey-patches in new methods & functionality.',
  author = 'David Carli-Arnold',
  author_email = 'davocarli@gmail.com',
  url = 'https://github.com/davocarli',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['Smartsheet', 'smartsheet-python-sdk', 'monkey-patch'],
  install_requires=[
          'smartsheet-python-sdk',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9'
  ],
)

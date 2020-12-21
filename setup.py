from distutils.core import setup
setup(
  name = 'smartools',
  packages = ['smartools'],
  version = '0.1',
  license='MIT',
  description = 'A class extending the official smartsheet-python-sdk that adds a new Util subclass with useful helper methods.',
  author = 'David Carli-Arnold',
  author_email = 'davocarli@gmail.com',
  url = 'https://github.com/davocarli',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Smartsheet', 'smartsheet-python-sdk', 'subclass'],
  install_requires=[            # I get to this in a second
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
  ],
)
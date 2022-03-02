from setuptools import setup, find_packages


setup(
  name = 'py-oiio',
  packages = ['oiio'],
  version = '0.0.1',
  license = 'MIT',
  description = 'OpenImageIO (OIIO) for Python',
  long_description_content_type="text/markdown",
  author = 'Noah Rahm',
  author_email = 'correctsyntax@yahoo.com',
  url = 'https://github.com/Correct-Syntax/py-oiio',
  keywords = ['openimageio', 'oiio'],
  classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.10',
  ],
  packages=find_packages(exclude=[]),
  package_data={
    # If any package (!) contains ... files, include them:
    "": [
        "*.pyd",
        "*.dll",
        "*.so",
    ]
  },
)

from setuptools import setup
import os


def is_package(path):
    return (os.path.isdir(path) and os.path.isfile(os.path.join(path, '__init__.py')))


def find_packages(path, base="" ):
    """ Find all packages in path """
    packages = {}
    for item in os.listdir(path):
        dir = os.path.join(path, item)
        if is_package( dir ):
            if base:
                module_name = "%(base)s.%(item)s" % vars()
            else:
                module_name = item
            packages[module_name] = dir
            packages.update(find_packages(dir, module_name))
    return packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name='cg_predict_price',
      version='0.3',
      description='Car Giant Predict Price of cars',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/MihaiBlebea/CarGiant-MachineLearning',
      author='Mihai Blebea',
      author_email='mihaiserban.blebea@gmail.com',
      license='MIT',
      packages=find_packages('.'),
      install_requires=[
          'beautifulsoup4',
          'certifi',
          'chardet',
          'et-xmlfile',
          'idna',
          'jdcal',
          'lxml',
          'MechanicalSoup',
          'numpy',
          'openpyxl',
          'pandas',
          'python-dateutil',
          'pytz',
          'requests',
          'scikit-learn',
          'scipy',
          'six',
          'sklearn',
          'urllib3',
          'xlrd',
      ],
      zip_safe=False)

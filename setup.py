from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name='cg_predict_price',
      version='0.1',
      description='Car Giant Predict Price of cars',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/MihaiBlebea/CarGiant-MachineLearning',
      author='Mihai Blebea',
      author_email='mihaiserban.blebea@gmail.com',
      license='MIT',
      packages=find_packages(),
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

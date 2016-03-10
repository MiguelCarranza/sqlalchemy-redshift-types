from setuptools import setup, find_packages

setup(name='sqlalchemy-redshift-types',
      version='0.1',
      description='Wrapper to only include SQLAlchemy types supported by Redshift',
      url='http://github.com/MiguelCarranza',
      author='Miguel Carranza',
      author_email='miguel@miguelcarranza.com',
      license='MIT',
      packages=['sqlalchemy_redshift_types'],
      install_requires = ['SQLAlchemy==1.0.8'],
      include_package_data = True,
      zip_safe=False)
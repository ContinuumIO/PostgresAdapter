PostgresAdapter
===============

PostgresAdapter is a Python module containing optimized data adapters for importing
data from PostgreSQL databases into NumPy arrays and Pandas DataFrame. It was
previously a part of the IOPro project.

Build Requirements
------------------

Building PostgresAdapter requires a number of dependencies. In addition to a C/C++ dev
environment, the following modules are needed, which can be installed via conda:

* NumPy 1.11
* Pandas
* postgresql 0.9.3 (C lib)

Building Conda Package
----------------------

Note: If building under Windows, make sure the following commands are issued
within the Visual Studio command prompt for version of Visual Studio that
matches the version of Python you're building for.  Python 2.6 and 2.7 needs
Visual Studio 2008, Python 3.3 and 3.4 needs Visual Studio 2010, and Python
3.5 needs Visual Studio 2015.

1. Install [Docker](https://docs.docker.com/engine/installation/). Add the current user to the `docker` group and restart the daemon, so that `docker` commands can be executed without root privileges

1. Build PostgresAdapter using the following command:
   `conda build buildscripts/condarecipe --python 3.5`

1. PostgresAdapter can now be installed from the built conda package:
   `conda install postgresadapter --use-local`

Building By Hand
----------------

Note: If building under Windows, make sure the following commands are issued
within the Visual Studio command prompt for version of Visual Studio that
matches the version of Python you're building for.  Python 2.6 and 2.7 needs
Visual Studio 2008, Python 3.3 and 3.4 needs Visual Studio 2010, and Python
3.5 needs Visual Studio 2015.

For building PostgresAdapter for local development/testing:

1. Install most of the above dependencies into environment called 'postgresadapter':
   `conda env create -f environment.yml`

   Be sure to activate new postgresadapter environment before proceeding.

1. Build PostgresAdapter using Cython/distutils:
   `python setup.py build_ext --inplace`

Testing
-------

To get a test database running, execute the following command (after [installing Docker](https://docs.docker.com/engine/installation/)):
```
docker run --name postgres-db --publish 5432:5432 -d mdillon/postgis:9.5-alpine
```

The Docker image is a ~150MB download. Once downloaded it should take about 10 seconds for the database to start. Once the database is up you may connect to it over the command line:
```
psql -h localhost -U postgres
```

Once the test database is running, generate the test data by executing the following script:
```
./postgresadapter/tests/setup_postgresql_data.py
```

Tests can be run by calling the postgresadapter module's test function:
```python
python -Wignore -c 'import postgresadapter; postgresadapter.test()'
```

To run the PostGIS tests, execute the following command:
```python
python -Wignore -c 'import postgresadapter; postgresadapter.test_postgis()'
```

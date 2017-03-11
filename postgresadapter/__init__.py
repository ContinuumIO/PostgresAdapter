"""
    PostgresAdapter
    ~~~~~

    PostgresAdapter provides tools to interface PostgreSQL databases in a fast,
    memory-efficient way.
"""
from __future__ import absolute_import

import sys
import os
import pytest

from postgresadapter._version import get_versions
__version__ = get_versions()['version']
del get_versions


from postgresadapter.core.PostgresAdapter import PostgresAdapter
from postgresadapter.lib.errors import (AdapterException, AdapterIndexError,
                                    ArgumentError, ConfigurationError,
                                    DataIndexError, DataTypeError,
                                    InternalInconsistencyError, NoSuchFieldError,
                                    ParserError, SourceError, SourceNotFoundError)


def test(host='localhost', dbname='postgres', user='postgres', verbose=True):
    test_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tests')        
    postgres_test_script = 'test_PostgresAdapter.py'
    args = []
    args.append(os.path.join(test_dir, postgres_test_script))
    args.append('--pg_host {0}'.format(host))
    args.append('--pg_dbname {0}'.format(dbname))
    args.append('--pg_user {0}'.format(user))
    if verbose:
        args.append('-v')

    result = pytest.main(' '.join(args))

    if result == 0:
        return True
    return False


def test_postgis(host='localhost', dbname='postgres', user='postgres', verbose=True):
    test_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tests')        
    postgis_test_script = 'test_PostGIS.py'
    args = []
    args.append(os.path.join(test_dir, postgis_test_script))
    if verbose:
        args.append('-v')

    result = pytest.main(' '.join(args))

    if result == 0:
        return True
    return False

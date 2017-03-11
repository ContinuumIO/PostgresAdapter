import subprocess
import postgresadapter
import os
import time
import inspect
from postgresadapter.tests import setup_postgresql_data



def start_postgres(waitsecs=10):
    subprocess.check_call('docker run --name postgres-db --publish 5432:5432 -d mdillon/postgis:9.5-alpine', shell=True)
    print('Waiting {} secs for PostgreSQL database to start up...'.format(waitsecs))
    time.sleep(waitsecs)


def stop_postgres(let_fail=False):
    try:
        subprocess.check_call('docker ps -q --filter "name=postgres-db" | xargs docker rm -vf', shell=True)
    except subprocess.CalledProcessError:
        if not let_fail:
            raise


### Run PostgreSQL tests
stop_postgres(let_fail=True)
start_postgres(waitsecs=10)
exec(inspect.getsource(setup_postgresql_data))
assert postgresadapter.test()

### Run PostGIS tests
#stop_postgres()
#start_postgres(waitsecs=10)
assert postgresadapter.test_postgis()
stop_postgres()

# Print the version
print('postgresadapter.__version__: %s' % postgresadapter.__version__)

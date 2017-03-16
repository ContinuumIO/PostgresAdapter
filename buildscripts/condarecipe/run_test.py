import subprocess
import postgresadapter
import os
import time
import atexit
import sys
import shlex
from postgresadapter.tests import setup_postgresql_data



def start_postgres():
    print('Starting PostgreSQL server...')

    cmd = shlex.split('docker run --name postgres-db --publish 5432:5432 mdillon/postgis:9.5-alpine')
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            universal_newlines=True)

    pg_init = False
    while True:
        output_line = proc.stdout.readline()
        print(output_line.rstrip())
        if proc.poll() is not None: # If the process exited
            raise Exception('PostgreSQL server failed to start up properly.')
        if 'PostgreSQL init process complete; ready for start up' in output_line:
            pg_init = True
        elif pg_init and 'database system is ready to accept connections' in output_line:
            break


def stop_postgres(let_fail=False):
    try:
        print('Stopping PostgreSQL server...')
        subprocess.check_call('docker ps -q --filter "name=postgres-db" | xargs docker rm -vf', shell=True)
    except subprocess.CalledProcessError:
        if not let_fail:
            raise


### Start PostgreSQL
stop_postgres(let_fail=True)
start_postgres()
atexit.register(stop_postgres)

### Run PostgresAdapter tests
setup_postgresql_data.main()
assert postgresadapter.test()

### Run PostGIS tests
assert postgresadapter.test_postgis()

# Print the version
print('postgresadapter.__version__: %s' % postgresadapter.__version__)

sys.exit(0)

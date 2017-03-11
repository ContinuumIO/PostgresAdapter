import os
import sys
import glob
from distutils.core import setup, Command
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy
import versioneer


class CleanInplace(Command):
    user_options = []

    def initialize_options(self):
        self.cwd = None

    def finalize_options(self):
        self.cwd = os.getcwd()

    def run(self):
        files = glob.glob('./postgresadapter/core/PostgresAdapter*.so')
        for file in files:
            try:
                os.remove(file)
            except OSError:
                pass


def setup_postgres(include_dirs, lib_dirs):
    src = ['postgresadapter/core/PostgresAdapter.pyx',
           'postgresadapter/core/postgres_adapter.c',
           'postgresadapter/core/postgis_fields.c',
           'postgresadapter/lib/converter_functions.c',
           'postgresadapter/lib/kstring.c']

    libraries = []
    if sys.platform == 'win32':
        libraries = ['libpq', 'ws2_32', 'secur32', 'shell32', 'advapi32']
    else:
        libraries = ['pq']

    return Extension('postgresadapter.core.PostgresAdapter',
                     src,
                     include_dirs=include_dirs,
                     libraries=libraries,
                     library_dirs=lib_dirs)


def run_setup():

    include_dirs = [os.path.join('postgresadapter', 'lib'),
                    numpy.get_include()]
    if sys.platform == 'win32':
        include_dirs.append(os.path.join(sys.prefix, 'Library', 'include'))
    else:
        include_dirs.append(os.path.join(sys.prefix, 'include'))

    lib_dirs = []
    if sys.platform == 'win32':
        lib_dirs.append(os.path.join(sys.prefix, 'Library', 'lib'))
    else:
        lib_dirs.append(os.path.join(sys.prefix, 'lib'))

    ext_modules = []
    packages = ['postgresadapter', 'postgresadapter.lib', 'postgresadapter.tests']

    ext_modules.append(setup_postgres(include_dirs, lib_dirs))
    packages.append('postgresadapter.core')

    versioneer.versionfile_source = 'postgresadapter/_version.py'
    versioneer.versionfile_build = 'postgresadapter/_version.py'
    versioneer.tag_prefix = ''
    versioneer.parentdir_prefix = 'postgresadapter-'

    cmdclass = versioneer.get_cmdclass()
    cmdclass['build_ext'] = build_ext
    cmdclass['cleanall'] = CleanInplace

    setup(name='postgresadapter',
          version = versioneer.get_version(),
          description='optimized IO for NumPy/Blaze',
          author='Jay Bourque',
          author_email='jay.bourque@continuum.io',
          ext_modules=ext_modules,
          packages=packages,
          cmdclass=cmdclass)


if __name__ == '__main__':
    run_setup()

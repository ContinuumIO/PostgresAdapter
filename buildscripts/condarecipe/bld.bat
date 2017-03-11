copy %LIBRARY_LIB%\boost_thread-vc90-mt-1_61.lib %LIBRARY_LIB%\libboost_thread-vc90-mt-1_61.lib
copy "C:\Program Files (x86)\Microsoft Visual Studio %VCD%\VC\%LDIR%\*.lib" %LIBRARY_LIB%\
%PYTHON% setup.py install
if errorlevel 1 exit 1

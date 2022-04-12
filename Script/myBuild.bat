
rem Set variables
if not defined STAR_SOURCE set STAR_SOURCE=%~dp0..
if not defined STAR_BUILD set STAR_BUILD=%STAR_SOURCE%\build

rem Set basic configuration
if not defined STAR_BUILD_TYPE set STAR_BUILD_TYPE=Release

rem build folder
if exist %STAR_BUILD% (
    echo "build folder exist"
) else (
    echo "add build folder"
    mkdir %STAR_BUILD%
)

rem Clean
del /F /Q "%STAR_BUILD%\%STRA_BUILD_TYPE%\cmake_install.cmake"
del /F /Q "%STAR_BUILD%\%STRA_BUILD_TYPE%\CMakeCache.txt"
del /F /Q "%STAR_BUILD%\%STRA_BUILD_TYPE%\CMakeFiles"

rem Configure
cd "%STAR_BUILD%"
cmake ..
cmake --build . --config="%STAR_BUILD_TYPE%"
goto:eof
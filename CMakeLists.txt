cmake_minimum_required(VERSION 3.10)

project(StarDEM VERSION 0.1)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

add_subdirectory(external_library/pybind11)
pybind11_add_module(StarDEM Constitutive/example.cpp)
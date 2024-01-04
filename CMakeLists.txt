cmake_minimum_required(VERSION 3.25)
project(casadi_codegen LANGUAGES C CXX)

set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
# include_directories("/Users/tudoroancea/Desktop/gsp/casadi_codegen")
# add_executable(main main.c gen.c)
add_executable(main main.cpp gen.c)
target_include_directories(main PUBLIC "/Users/tudoroancea/Desktop/gsp/casadi_codegen")


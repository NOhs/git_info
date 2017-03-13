# Defines macro that allows people to inject a header
# into their source tree.
#
# Requires: Python >= 3.5
#
# Usage: If header_path_name is the path/name where to
#        inject the header to
#
# >>> create_git_info_header_target("myFolder/myHeaderName.hpp")
#

cmake_minimum_required(VERSION 3.6)
project(git_info CXX)

find_package(PythonInterp 3.5 REQUIRED)

set_property(GLOBAL PROPERTY git_info_script_path ${CMAKE_CURRENT_LIST_DIR})

macro(create_git_info_file header_path_name language)
    get_property(_filepath GLOBAL PROPERTY git_info_script_path)

    if(${language} STREQUAL "cpp")
        set(header_in "${_filepath}/git_info.hpp.in")
    elseif(${language} STREQUAL "python")
        set(header_in "${_filepath}/git_info.py.in")
    else()
        message(SEND_ERROR "Language ${language} for git_info is not defined.")
    endif()   

    set(header_tmp "${_filepath}/git_info_${language}.tmp")

    add_custom_command(
        OUTPUT ${header_tmp}
        COMMAND ${PYTHON_EXECUTABLE} ${_filepath}/create_git_info_header.py ${header_in} ${language} ${header_tmp}
        COMMAND ${CMAKE_COMMAND} -E copy_if_different ${header_tmp} ${header_path_name}
        COMMAND ${CMAKE_COMMAND} -E remove ${header_tmp}        
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})
    
    add_custom_target(git_info_file_${language} DEPENDS ${header_tmp})
    unset(header_in)
    unset(header_tmp)
endmacro(create_git_info_file header_path_name)

if(${CMAKE_SOURCE_DIR} STREQUAL ${CMAKE_CURRENT_SOURCE_DIR})
    create_git_info_file(test.hpp cpp)
    create_git_info_file(test.py python)

    add_executable(my_test main.cpp)
    add_dependencies(my_test git_info_file_cpp)

    add_executable(my_test2 main.cpp)
    add_dependencies(my_test2 git_info_file_python)
endif()

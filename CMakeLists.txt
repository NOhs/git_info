# Defines macro that allows people to inject a header
# into their source tree.
#
# Requires: Python >= 3.5
#
# Usage: Call the defined macro `create_git_info_file`.
#        The first argument should be a full file-pathname to
#        where the info_file should be created. The second argument
#        determines the language. Options are:
#          - cpp
#          - python
#
#       A CMake variable IS_GIT_REPOSITORY is defined so you can check
#       if you are actually in a git repository.
#
# >>> add_subdirectory(path_to_git_info_folder)
# >>> if(IS_GIT_REPOSITORY)
# >>>     create_git_info_file("${my_source_folder}/git_info.hpp" cpp)
# >>> else()
# >>>     roll custom solution for version file you might have
# >>> endif(IS_GIT_REPOSITORY)
#

cmake_minimum_required(VERSION 3.6)
project(git_info CXX)

find_package(Git REQUIRED)
find_package(PythonInterp 3.5 REQUIRED)

set_property(GLOBAL PROPERTY git_info_script_path ${CMAKE_CURRENT_LIST_DIR})
execute_process(
    COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_LIST_DIR}/check_in_git_repository.py 
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    OUTPUT_VARIABLE _IS_GIT_REPOSITORY)

set(IS_GIT_REPOSITORY ${_IS_GIT_REPOSITORY})
unset(_IS_GIT_REPOSITORY)

macro(create_git_info_file header_path_name language)
    get_property(_filepath GLOBAL PROPERTY git_info_script_path)

    if(${language} STREQUAL "cpp")
        set(header_in "${_filepath}/git_info.hpp.in")
    elseif(${language} STREQUAL "python")
        set(header_in "${_filepath}/git_info.py.in")
    else()
        message(SEND_ERROR "Language ${language} for git_info is not defined.")
    endif()   

    set(header_tmp "${CMAKE_CURRENT_BINARY_DIR}/git_info_${language}.tmp")

    add_custom_command(
        OUTPUT ${header_tmp}
        COMMAND ${PYTHON_EXECUTABLE} ${_filepath}/create_git_info_header.py ${header_in} ${language} ${header_tmp}
        COMMAND ${CMAKE_COMMAND} -E copy_if_different ${header_tmp} ${header_path_name}
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})
    
    add_custom_target(git_info_file_${language} ALL DEPENDS ${header_tmp})
    unset(header_in)
    unset(header_tmp)
    unset(_filepath)
endmacro(create_git_info_file header_path_name language)

find_package_handle_standard_args(Git_Info
                                  REQUIRED_VARS IS_GIT_REPOSITORY)

if(${CMAKE_SOURCE_DIR} STREQUAL ${CMAKE_CURRENT_SOURCE_DIR})
    create_git_info_file(test/git_info.hpp cpp)
    create_git_info_file(test/git_info.py python)
    
    enable_testing()

    add_test(
        NAME              test_cpp_compile 
        COMMAND           sh test_cpp_compiles.sh
        WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/test)

    add_test(
        NAME              test_python_works
        COMMAND           sh test_python_runs.sh
        WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/test)

    add_test(
        NAME              test_python_cpp_output_equal
        COMMAND           sh compare_cpp_python_output.sh
        WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/test)

    message(${IS_GIT_REPOSITORY})
endif()

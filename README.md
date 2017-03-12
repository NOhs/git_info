# git_info
A CMake script that provides git-repository information as C++ header or python files.

## For the impatient
### Installation
Just copy the project as a subfolder into your project.
### Usage
This simple demo shows how you can use git_info in your project.
```cmake
cmake_minimum_required(VERSION 3.6)
project(my_awesome_project CXX)

# Adding this subdirectory will make the macro `create_git_info_file` available
# Currently this can be called with cpp or python
# The name of the file is your choice
add_subdirectory(path/to/git_info)
create_git_info_file(headers/my_git_info_header.hpp cpp)

add_executable(my_test src/main.cpp)
# The call to `create_git_info_file` with parameter cpp makes this dependency
# available, if the macro above was called with python, the target would end
# with `_python`
add_dependencies(my_test git_info_file_cpp)
```

## Overview
It is often desirable to store some kind of version number of your code in your executable.
Manually keeping track of it is tedious and prone to errors. Doing it automatically in CMake often
seems to be quite tedious, too, having to work around the fact that `configure_file` is
only called during project creation and not before each build etc. Some solutions available
online also introduce extra source files one has to take care of, which makes these solutions
even more unattractive.

Therefore, the design goals for this script were:
- Header only for C++ projects
- Using a python script to keep the CMake code simple and short
- Providing a simple way to include the header file the way the user wants
  - keep location flexible
  - keep name flexible
- Keeping CMake usage simple

### Header only
Using constexpr variable, the implementation should not have any overhead, while
keeping all the advantages of variables compared to `#define`s. All functions are in a single
namespace, keeping the global namespace clean. Being header only, developers do not have
to remember to add source files from this file to their build targets.

### Using a python script
There are two main reasons, why the main script generation was done in python.
Number one being that I really prefer writing code in python. Number two being that
if people use a different build system for their project, they can still use the
python part most likely.

### Providing a simple way
Some solutions online add the "unclear" location of the created header to
the include directories, so that people can just use the header. However, 
it is more transparent, if programmers can place the header in the location
of their choice, with a name of their choice. After all, if this later appears
as part of some documentation, it makes sense, that this header file has a
clear location inside the project.

### Keeping CMake usage simple
Nothing is more useless than a solution that requires as many lines to use
as it would take to rewrite the solution. So keeping it short and simple when
used is part of the idea of this project. This also means that before each build
the git information is updated without any manual CMake solution re-creation.

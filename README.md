# git_info
A CMake script that provides git-repository information as C++ header or python files.
### Table of contents

* [For the impatient](#for_the_impatient)
    * [Installation](#installation)
    * [Usage](#usage)
* [Overview](#overview)
    * [Header only](#header_only)
    * [Using a python script](#using_a_python_script)
    * [Providing a flexible way](#providing_a_flexible_way)
    * [Keeping cmake usage simple](#keeping_cmake_usage_simple)
* [Exported files](#exported_files)
    * [C++](#cpp)
    * [Python](#python)


## For the impatient<a name="for_the_impatient"></a>
### Installation<a name="installation"></a>
Just copy the project as a subfolder into your project.
### Usage<a name="usage"></a>
This simple demo shows how you can use git_info in your project.
```cmake
cmake_minimum_required(VERSION 3.6)
project(my_awesome_project CXX)

# Adding this subdirectory will make the macro `create_git_info_file` available
# Currently this can be called with cpp or python
# The name of the file is your choice
add_subdirectory(path/to/git_info)

add_executable(my_test src/main.cpp)

if(IS_GIT_REPOSITORY)
    create_git_info_file(headers/my_git_info_header.hpp cpp)

    # The call to `create_git_info_file` with parameter cpp makes this target
    # available as a dependency. If the macro above was called with python, the target would end
    # with `_python`
    add_dependencies(my_test git_info_file_cpp)
else()
    # Read in your version file or whatever
endif(IS_GIT_REPOSITORY)



```

## Overview<a name="overview"></a>
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

### Header only<a name="header_only"></a>
Using constexpr variable, the implementation should not have any overhead, while
keeping all the advantages of variables compared to `#define`s. All functions are in a single
namespace, keeping the global namespace clean. Being header only, developers do not have
to remember to add source files from this file to their build targets.

### Using a python script<a name="using_a_python_script"></a>
There are two main reasons, why the main script generation was done in python.
Number one being that I really prefer writing code in python. Number two being that
if people use a different build system for their project, they can still use the
python part most likely.

### Providing a flexible way<a name="providing_a_flexible_way"></a>
Some solutions online add the "unclear" location of the created header to
the include directories, so that people can just use the header. However, 
it is more transparent, if programmers can place the header in the location
of their choice, with a name of their choice. After all, if this later appears
as part of some documentation, it makes sense, that this header file has a
clear location inside the project.

### Keeping CMake usage simple<a name="keeping_cmake_usage_simple"></a>
Nothing is more useless than a solution that requires as many lines to use
as it would take to rewrite the solution. So keeping it short and simple when
used is part of the idea of this project. This also means that before each build
the git information is updated without any manual CMake solution re-creation.

## Exported files<a name="exported_files"></a>
Once the files have been created, the following functionality is available.
### C++<a name="cpp"></a>
The generated header file offers several variables that are all bundled in the
namespace `git_info`. The file is fully equipped with doxygen comments, so once
you include them into your project, you can look up the exact definitions of the
variables in your own documentation.

A brief list of the variables:

```cpp
constexpr char SHA1[]
constexpr bool IS_DIRTY
constexpr char BRANCH[]
constexpr char SHA1_PRETTY[]
constexpr char LAST_COMMIT_TIME[]
constexpr char LAST_COMMIT_SUBJECT[]
```

### Python<a name="python"></a>
Similar to the C++ example above, the python file also contains a set of variables with documentation of each in the
module doc_string.

```python
SHA1
IS_DIRTY
BRANCH
SHA1_PRETTY
LAST_COMMIT_TIME
LAST_COMMIT_SUBJECT
```

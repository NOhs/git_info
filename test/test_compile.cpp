#include <iostream>
#include "git_info.hpp"

int main()
{
    std::cout << "SHA1:  " << git_info::SHA1 << "\n";
    std::cout << "Is dirty:  " << (git_info::IS_DIRTY ? "True" : "False") << "\n";
    std::cout << "Branch name:  " << git_info::BRANCH << "\n";
    std::cout << "SHA1 pretty:  " << git_info::SHA1_PRETTY << "\n";
    std::cout << "Commit time:  " << git_info::LAST_COMMIT_TIME << "\n";
    std::cout << "Last commit subject:  " << git_info::LAST_COMMIT_SUBJECT << "\n";
}

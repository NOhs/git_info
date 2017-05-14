#include <fstream>
#include "git_info.hpp"

int main()
{
    std::ofstream myfile;
    myfile.open("cpp_git.out");

    myfile << "SHA1:  " << git_info::SHA1 << "\n";
    myfile << "Is dirty:  " << (git_info::IS_DIRTY ? "True" : "False") << "\n";
    myfile << "Branch name:  " << git_info::BRANCH << "\n";
    myfile << "SHA1 pretty:  " << git_info::SHA1_PRETTY << "\n";
    myfile << "Commit time:  " << git_info::LAST_COMMIT_TIME << "\n";
    myfile << "Last commit subject:  " << git_info::LAST_COMMIT_SUBJECT << "\n";
}

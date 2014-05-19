// chapter 1 question 1
/*
 write a method to replace all spaces in a string with '%20'. you may assume that the string has sufficient space at the end of the string to hold the addditional chas, and that you are given the 'true' length of the string. (note: if using java, use a char aarray)
EXAMPLE
input: "Mr John Smith    "
output: "Mr%20John%20..."
*/


#include <string>

using namespace std;


//this is the simplest implementation, better performance if used ctrings

string replaceSpace(string str)
{
    string retStr = str;
    size_t spacePos = 0;
    while (string::npos != (spacePos = retStr.find(' '))){ //find is O(N) each time
        retStr.replace(spacePos, 1, "%20"); // O(N) and creating a brand new string each time, i think?
    }
    return retStr;
}

int main()
{

    string s = "nospace";
    printf("||%s||%s||\n", s.c_str(), replaceSpace(s).c_str());
    s = "one space";
    printf("||%s||%s||\n", s.c_str(), replaceSpace(s).c_str());
    s = " lots of  spaces    ";
    printf("||%s||%s||\n", s.c_str(), replaceSpace(s).c_str());
    s = "";
    printf("||%s||%s||\n", s.c_str(), replaceSpace(s).c_str());
    

  return 0;
}

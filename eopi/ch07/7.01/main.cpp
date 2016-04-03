#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

int atoi(string &str) {
    int ret = 0;
    bool is_negative = false; 
    for (size_t i=0; i<str.size(); ++i) {
        char c = str.at(i);
        //if (c == "-") {

        if (i==0) && (strncmp(str.c_str(), "-", 1) == 0) {
            is_negative = true;
            continue;
        }
        int digit = int(str.at(i) - 48);
        ret = ret*10 + digit;
    }

    return is_negative ? ret*-1 : ret;
}

int main(void)
{
    string mystr = "-23";
    cout <<  atoi(mystr);
    return 0;
}

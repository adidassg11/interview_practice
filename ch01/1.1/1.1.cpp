// chapter 1 question 1
// implement an algorithm to determine if a string has all uniqe characters. what if you cannot use additional data structures?

#include <string>
#include <bitset>

using namespace std;

#define BITSET_LEN 256

bool allUnique1(const char * str)
{
    printf("testing word: %s\n", str);

    int strLen = strlen(str);
    printf("len: %d\n", strLen);
    bitset<BITSET_LEN> bs;

    for(int i=0; i<strLen; i++){
        if(bs[str[i]]) {
            printf("FALSE\n");
            return false;
        }
        bs[str[i]] = 1;
    }

    printf("TRUE\n");
    return true;
}

int main()
{
    string string1 = "asdf";
    allUnique1(string1.c_str());
    const char* s2 = "asdfa";
    allUnique1(s2);
    const char* s3 = "asdff";
    allUnique1(s3);
    const char* s4 = "1111";
    allUnique1(s4);
    const char* s5 = "1234567890qwertyuiopasdfghjklzxcvbnm!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:";
    allUnique1(s5);
    const char* s6 = "1234567890qwertyuiopasdfghjklzxcvbnm!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:a";
    allUnique1(s6);
    
    
    return 0;
}

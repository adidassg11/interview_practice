// chapter 1 question 3
// given two strings, write a method to decide if one is a permutation of the other

#include <string>

//for perm1 where we sort the chars then walk thru and compare
#include <algorithm>
#include <array>

//for perm2 where we use c++ strings
#include <string>
#include <iostream>

#define NUMCHAR 256

using namespace std;

bool isPerm1() {
    return true;
}

//uses c++ strings
//seems to work with everything except \0 char
// FIX - use the string.compare() function!
bool isPerm2(string s1, string s2) {
    printf("\tisPerm2(%s , %s)\n",s1.c_str(), s2.c_str());

    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());
    printf("\t\t%s\n", s1.c_str());
    printf("\t\t%s\n", s2.c_str());

    bool isSorted = (s1==s2);
    bool isSorted2 = ~s1.compare(s2);

    isSorted ? printf("\tIs Permutation\n") : printf("\tNot Permutation\n");
    isSorted2 ? printf("\tIs Permutation\n") : printf("\tNot Permutation\n");
    
    return isSorted;
}


bool isPerm(char* s1, char* s2) {
    printf("s1: %s\ns2: %s\n", s1, s2);
    
    bool isPerm = false;
    char* charArr = new char[NUMCHAR];

    printf("charArr: %s\n", charArr);
    memset(charArr, 0, NUMCHAR*sizeof(char));
    printf("charArr: %s\n", charArr);
    
    

    printf("Is perm? %s\n", isPerm ? "TRUE" : "FALSE"); 

    delete [] charArr;
    return isPerm; 
}

int main()
{
    char s1[] = "anna";
    char s2[] = "naan";

    isPerm2(s1, s2);

    char s3[] = "asodifjaw";
    char s4[] = "waiefojawoef";
    isPerm2(s3, s4);

    char s5[] = "83\09r\ruji\nofwd$)j\tf ";
    char s6[] = "\03\r9ruji\nofwd$)jf 8\t";
    isPerm2(s5, s6);

    return 0;
}

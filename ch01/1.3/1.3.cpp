// chapter 1 question 3
// given two strings, write a method to decide if one is a permutation of the other


#include <string>

#define NUMCHAR 256

using namespace std;

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

    isPerm(s1, s2);

//    isPerm("asdf", "aasdf");

    return 0;
}

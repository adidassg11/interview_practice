// chapter 1 question 2
// implement a function void reverse(char* str) in C or c++ which reverses a null -terminated string

#include <strings.h> //use cstirngs
#include <stdio.h> //printf

//using namespace std;

//assumes null terminated
void reverse(char* s)
{
    printf("string: %s\n", s);
    size_t len = strlen(s);
    for(char i=0; i<len/2; i++){
        char tmp = s[i];
        s[i] = s[len-i-1];
        s[len-i-1] = tmp;
    } 

    printf("reversed string: %s\n", s);
}

int main()
{
    char s1[] = "asdf";
    reverse(s1);

    char s2[] = "1234567890-=!@#$%^&*()_+";
    reverse(s2);

    char s3[] = "";
    reverse(s3);

    char s4[] = "12345";
    reverse(s4);
    
  return 0;
}

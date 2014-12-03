#include <stdio.h>

unsigned long long fact(int i) {
    unsigned long long fact = 1;
    for(int i=1; i<30; i++) {
       fact = fact*i;
//        printf("fact(%d): %llu\n", i, fact);
    } 
    return fact;
}

//finds numZeros in n!
int numZeros(int n) {
    int numTens = n/10; //each factor of 10 (20, 30, 90, etc) adds a zero
    int numFives = numTens + (n%10>=5);
    return numFives + numTens;  
}

int main(void) {
    int i = 1;
    printf("fact %d: %llu numZeros: %d\n", i, fact(i), numZeros(i));
    i = 4;
    printf("fact %d: %llu numZeros: %d\n", i, fact(i), numZeros(i));
    i = 5;
    printf("fact %d: %llu numZeros: %d\n", i, fact(i), numZeros(i));
    i = 9;
    printf("fact %d: %llu numZeros: %d\n", i, fact(i), numZeros(i));
    i = 10;
    printf("fact %d: %llu numZeros: %d\n", i, fact(i), numZeros(i));
    i = 14;
    printf("fact %d: %llu numZeros: %d\n", i, fact(i), numZeros(i));
    i = 15;
    printf("fact %d: %llu numZeros: %d\n", i, fact(i), numZeros(i));
    i = 19;
    printf("fact %d: %llu numZeros: %d\n", i, fact(i), numZeros(i));
    i = 20;
    printf("fact %d: %llu numZeros: %d\n", i, fact(i), numZeros(i));
    

    return 0;
}

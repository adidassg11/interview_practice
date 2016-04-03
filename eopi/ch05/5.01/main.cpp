/*
just trying to find an algo/equation...

1101 xor 1101-1
0001 xor 0001-1 1
000 2

1100 xor 1100-1 (1011)
0111 xor 0111-1 (0110) 1
0001 xor 0001-1  2
0000   3

1111 xor 1111-1 (1110)
0001 xor 0001-1  1
0000  2


0101 

*/

#include <stdio.h>

bool isOddParity(long long num) {
    printf("isOddParity(%lld)\n", num);
    int ctr = 0;
    long long x = num; //xor
    while (x != 1) {
        x ^= (x -1);
        printf("x is: %lld\n", x);
        ctr ++;
    }
    
    return (ctr%2); 
}

int main(void) {
    long long n1 = 0xD; //0b1101
    printf("%lld is %s parity\n", n1, isOddParity(n1)?"odd":"even");
    n1 = 0xC;
    printf("%lld is %s parity\n", n1, isOddParity(n1)?"odd":"even");
    n1 = 0xF;
    printf("%lld is %s parity\n", n1, isOddParity(n1)?"odd":"even");
    
    return 0;
}

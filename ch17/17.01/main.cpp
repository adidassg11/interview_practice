#include <stdio.h>

void numSwap(int num1, int num2) {
    printf("numSwap %d %d\n", num1, num2); 
    num1 ^= num2;
    num2 ^= num1;
    num1 ^= num2;
    printf("swapped: %d %d\n", num1, num2); 
}

int main(void) {
    numSwap(1, 2);
    numSwap(105238, -172342);
    numSwap(-12374779, -92834721);
    numSwap(0, MAX_INT);

    return 0;
}

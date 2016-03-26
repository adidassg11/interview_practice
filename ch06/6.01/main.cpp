// TODO: not finished, compile errors

#include <stdio.h>

void arrange(int* a, unsigned int n, unsigned int x)
{
    int num = a[x];
    int skip = x;
    unsigned int next_p = 0; //next place to put a new number in array
    
    for(int i = 0; i<n; i++) {
        if (i==x) continue;
        if (a[i] < num) {
            a[next_p] = a[i];
            //increase next_p
            next_p++;
            if (next_p == num) next_p++;
        }
    }
}

void print_array(int* a, unsigned int len) {
    printf("array: ");
    for (int i=0; i<len; i++) {
        printf("%u ", a[len]);
    }
    printf("\n");
}

int main(void)
{
    printf("hello\n");
    unsigned int len = 6;
    unsigned int a[6] = { 3, 2, 1, 3, 2, 1};
    print_array(a, len); 
    return 0;
}

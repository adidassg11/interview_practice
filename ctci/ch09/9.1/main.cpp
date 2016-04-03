#include <stdio.h>
#include <array>
#include <stdlib.h>

using namespace std;

#define ARRAY_SIZE 20

int howManyWays(int step, array<int, 20> &ways)
{

    printf("howManyWays() step %d\n", step);
    // Error case
    if (step < 0) {
        printf("howManyWays() step < 0\n");
        return 0;
    }

    // Base cases
    // Probably not the most efficient way of doing things here
    if (ways[step]) return ways[step];
    if (step == 0) {
        ways[0] = 0;
        return ways[0];
    }
    if (step == 1) {
        ways[1] = 1;
        return ways[1];
    }

    ways[step] = 0;
    // Main Dynamic algorithm
    if (step >=3) {
        printf("step-3; %d ways %d\n", (step-3), howManyWays(step-3, ways));
        ways[step] += (0 + howManyWays(step-3, ways));
    }
    if (step >=2) { 
        printf("step-2; %d ways %d\n", (step-2), howManyWays(step-2, ways));
        ways[step] += (0 + howManyWays(step-2, ways));
    }
    if (step >=1) {
        printf("step-1; %d ways %d\n", (step-1), howManyWays(step-1, ways));
        ways[step] += (0 + howManyWays(step-1, ways));
    }

    return ways[step];
}

int howManyWays2(int step, array<int, 20> &ways)
{
    printf("howManyWays2()\n");
    
    if (step < 1) {
        return 0;
    }

    if (step == 1) {
        ways[1] = 1;
        return ways[1];
    }


    ways[step] += howManyWays2(step-3, ways) 
                + howManyWays2(step-2, ways) 
                + howManyWays2(step-1, ways);

    return ways[step];
}

void printArray(array<int, ARRAY_SIZE> &a)
{
    printf("printArray: ");
    for (int i = 0; i<a.size(); ++i) {
        printf("%d ", a[i]);
    }
    printf("\n");
}

int main(void)
{
    printf("      Problem 9.1      \n");
    printf("= = = = = = = = = = = =\n");

    array<int, ARRAY_SIZE> a;
    a.fill(0);
    //howManyWays(5, a);
    howManyWays2(5, a);
    printArray(a);

    return 0;
}

#include <stdlib.h>
#include <stdio.h>
#include <time.h>

//#define rand5 randX(5)

void printRandXStats(int numCycles, int X) {
    time_t timeVar;
    printf("Time: %d\n", (int)time(&timeVar));

    printf("Rand%d\n", X);
    srand(timeVar);
    int randNum = rand();
    
    int numZeros = 0;
    int numOnes = 0;
    int numTwos = 0;
    int numThrees = 0;
    int numFours = 0;
    int numFives = 0;
    int num6s, num7s, num8s, num9s;
    num6s = num7s = num8s = num9s = 0;

    printf("getting rand for %d cycles\n", numCycles);
    for(int i=0; i<numCycles; i++) {
// RAND FUNC
//        int newNum = rand()%X; //this is perfect for <=10
        
        int newNum = 0;
        for(int i = 0; i<10; i++) {
            //newNum+=10*i*(rand()%X);
            newNum+=10*i*(rand());
        }
        newNum%=X;       
        switch (newNum) {
            case 0: numZeros++; break;
            case 1: numOnes++; break;
            case 2: numTwos++; break;
            case 3: numThrees++; break;
            case 4: numFours++; break;
            case 5: numFives++; break;
            case 6: num6s++; break;
            case 7: num7s++; break;
            case 8: num8s++; break;
            case 9: num9s++; break;
        }
    }

    printf("0s: %d\n1s: %d\n2s: %d\n3s: %d\n4s: %d\n5s: %d\n6s: %d\n7s: %d\n8s: %d\n9s: %d\n", numZeros, numOnes, numTwos, numThrees, numFours, numFives, num6s, num7s, num8s, num9s);


}

int randX(int x) {
    time_t timeVar;
    srand(time(&timeVar));

    return rand()%x;
}

//this is bad, it gives 6 7 8 more often
int rand5x2() {
    time_t timeVar;
    srand(time(&timeVar));
    

    return rand()%5 + rand()%5;
}



int main(void) {
    printRandXStats(400000, 2);
    printRandXStats(400000, 3);
    printRandXStats(400000, 4);
    printRandXStats(400000, 5);
    printRandXStats(400000, 6);
    printRandXStats(400000, 7);
    printRandXStats(400000, 8);
    printRandXStats(400000, 9);
    printRandXStats(400000, 10);

    printf("rand5: %d\n", randX(5));

    return 0; 
}

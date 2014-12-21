#include "helpers.h"

#include <stdio.h>
#include <map>
#include <stdlib.h>

using namespace std;

void printCoinSet(CoinSet* c)
{
    printf("CoinSet %p: total: %d value: %d coins: ", c, c->numTotal, c->value);

    for (int i = 0; i<c->numQ; ++i) {
        printf("Q");
    }
    for (int i = 0; i<c->numD; ++i) {
        printf("D");
    }
    for (int i = 0; i<c->numN; ++i) {
        printf("N");
    }
    for (int i = 0; i<c->numP; ++i) {
        printf("P");
    }

    printf("\n");
}

void printCoinMap(map<int, CoinSet*> &coinMap)
{
    map<int, CoinSet*>::iterator i;
    for ( i = coinMap.begin(); i!=coinMap.end(); ++i) {
        printf("coin %p value %d\n", &i, i->first);
        printCoinSet(i->second);
    }
}

void deleteCoins(map<int, CoinSet*> &coinMap)
{
    printf("Deleting coins...\n");
    map<int, CoinSet*>::iterator i;
    for ( i = coinMap.begin(); i!=coinMap.end(); ++i) {
        printf("CoinSet value %d\n", i->first);
        delete i->second;
    }
}

///TODO: should just add this in the CoinSet struct/class
void copyCS(CoinSet* srcCS, CoinSet* newCS)
{
    if (!srcCS || !newCS) {
        printf("NULL in copyCS()\n");
        exit(1);
    }

    newCS->numQ = srcCS->numQ;
    newCS->numD = srcCS->numD;
    newCS->numN = srcCS->numN;
    newCS->numP = srcCS->numP;
    newCS->numTotal = srcCS->numTotal;
    newCS->value = srcCS->value;
}


// All the coinset internals
int CoinSet::subQ() {
    if (numQ < 1) {
        printf("Error in SubQ()\n");
        return -1;
    }
    numQ--;
    numTotal--;
    value-=25;
    return 0;
}

int CoinSet::subD() {
    if (numD < 1) {
        printf("Error in SubD()\n");
        return -1;
    }
    numD--;
    numTotal--;
    value-=10;
    return 0;
}

int CoinSet::subN() {
    if (numN < 1) {
        printf("Error in SubN()\n");
        return -1;
    }
    numN--;
    numTotal--;
    value-=5;
    return 0;
}

int CoinSet::subP() {
    if (numP < 1) {
        printf("Error in SubP()\n");
        return -1;
    }
    numP--;
    numTotal--;
    value-=1;
    return 0;
}

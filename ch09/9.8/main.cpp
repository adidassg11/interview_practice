#include <stdio.h>
#include <map>

#include "helpers.h"

using namespace std;

typedef pair<int, CoinSet*> CoinPair;

//just going to do most efficient sets, not all sets
int buildMap(int targetVal, map<int, CoinSet*> &coinMap)
{
    if (targetVal < 0) return -1;

    //if it exists, do nothing
    if (coinMap.find(targetVal) != coinMap.end()) return 0;

    if (targetVal == 1) {
        CoinSet* cs = new CoinSet(0,0,0,1,1,1);
        coinMap.insert(CoinPair(1, cs));
        return 0;
    }

    map<int, CoinSet*>::iterator map_it;

    buildMap(targetVal-24, coinMap);
    map_it = coinMap.find(targetVal - 24);
    if (map_it != coinMap.end()) {
        CoinSet* newCS = new CoinSet();
        //copy old to new then update
        copyCS(map_it->second, newCS);
        newCS->numQ++;
        newCS->numTotal++;
        newCS->value+=25;
        coinMap.insert(CoinPair(targetVal, newCS));
        return 0;
    }


    buildMap(targetVal-9, coinMap);
    map_it = coinMap.find(targetVal - 9);
    if (map_it != coinMap.end()) {
        CoinSet* newCS = new CoinSet();
        //copy old to new then update
        copyCS(map_it->second, newCS);
         //if (!newCS->subN()) {
         if (!newCS->subN() && !newCS->subP() &&
            !newCS->subP() && !newCS->subP() 
            && !newCS->subP()) {
            newCS->numD++;
            newCS->numTotal++;
            newCS->value+=10;
            coinMap.insert(CoinPair(targetVal, newCS));
            return 0;
        }
        if (!newCS->subP()) {
            newCS->numD++;
            newCS->numTotal++;
            newCS->value+=10;
            coinMap.insert(CoinPair(targetVal, newCS));
            return 0;
        }
    }
        
    buildMap(targetVal-4, coinMap);
    map_it = coinMap.find(targetVal - 4);
    if (map_it != coinMap.end()) {
        CoinSet* newCS = new CoinSet();
        //copy old to new then update
        copyCS(map_it->second, newCS);
        if (!newCS->subP()) {
            newCS->numN++;
            newCS->numTotal++;
            newCS->value+=5;
            coinMap.insert(CoinPair(targetVal, newCS));
        }
        //else??? 
    }


    buildMap(targetVal-1, coinMap);
    map_it = coinMap.find(targetVal - 1);
    if (map_it != coinMap.end()) {
        CoinSet* newCS = new CoinSet();
        //copy old to new then update
        copyCS(map_it->second, newCS);
        newCS->numP++;
        newCS->numTotal++;
        newCS->value+=1;
        coinMap.insert(CoinPair(targetVal, newCS));
    }

    printf("X\n");
    return 0;
}


int main(void)
{
    printf("      Problem 9.8      \n");
    printf("= = = = = = = = = = = =\n");

/*
    map<int, CoinSet*> coinMap;
    CoinSet* c1 = new CoinSet(1, 1, 1, 1, 4, 41);
    CoinSet* c2 = new CoinSet(0, 0, 1, 1, 2, 6);
    CoinSet* c3 = new CoinSet(0, 0, 0, 9, 9, 9);

    coinMap.insert(pair<int, CoinSet*>(c1->value, c1));
    coinMap.insert(pair<int, CoinSet*>(c2->value, c2));
    coinMap.insert(pair<int, CoinSet*>(c3->value, c3));
    printCoinMap(coinMap);
    deleteCoins(coinMap);
    */
    
    map<int, CoinSet*> coinMap;
    //buildMap(1, coinMap);    
    buildMap(24, coinMap);    
    printCoinMap(coinMap);
    deleteCoins(coinMap);

    return 0;
}

#ifndef _9_8_HELPERS
#define _9_8_HELPERS

#include <map>

using namespace std;

struct CoinSet {
    CoinSet(int _q = 0, int _d = 0, int _n = 0, int _p = 0, int _t = 0, 
                                    int _v = 0) :   numQ(_q),
                                                    numD(_d),
                                                    numN(_n),
                                                    numP(_p),
                                                    numTotal(_t),
                                                    value(_v) {}
    int numQ; // quarters
    int numD; // nickels
    int numN; // dimes
    int numP; // pennies
    int numTotal;
    int value;

    int subQ();
    int subD();
    int subN();
    int subP();
};

void printCoinSet(CoinSet* c);
void printCoinMap(map<int, CoinSet*> &coinMap);
void deleteCoins(map<int, CoinSet*> &coinMap);
void copyCS(CoinSet* origCS, CoinSet* newCS);

// All the CoinSet internals

#endif //_9_8_helpers



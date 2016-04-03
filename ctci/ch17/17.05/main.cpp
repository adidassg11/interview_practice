#include <stdio.h>
#include <string>
#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

//mastermind with 4 slots
//sanswer, sguess
void mm4(string sa, string sg) {
    cout << "answer: " << sa << " guess: " << sg << endl;
    //use a set for add and remove in a more general solution? would it be O(1)?

    string eb = ""; //extra blue, etc.
    string eg = "";
    string er = "";
    string ey = "";

    set<char> setAnswers; //doesn't include the hits
    set<char> setGuesses; //doesn't include the hits
 
    for(int i = 0; i<sa.length(); i++) {
        if (sa[i] == sg[i]) {
            cout << "Hit on " << sa[i] << endl;
        }
        else {
            setAnswers.insert(sa[i]);
            setGuesses.insert(sg[i]);
        }
    }
    
//TODO: this stuff
    set<string> setInter;
    set<string>::iterator it;

    it = set_intersection(setAnswers.begin(), setAnswers.end(), setGuesses.begin(), setGuesses.end(), setInter.begin());
    
}

int main(void) {
    printf("17.05 - Mastermind\n");
    string test = "teststring";
    std::cout << "test: " << test << std::endl;
    printf("string: %s\n", test.c_str());

    mm4("RGBY", "GGRR");

    return 0;
}

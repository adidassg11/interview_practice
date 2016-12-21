/* Solution:
just sort copy the array, sort the copy, and compare to the original. O(N) mem, O(nlogn + n) runtime

slightly better:
Build bst from array as you iterate over it, keep inserting new number and if it is less than max, store its index. This is less than nlogn because each insertion is only on part of the dataset (except for the last insertion into the tree)
*/

#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

void sortPractice() {
    vector<int> v;
    v.push_back(2);
    v.push_back(10);
    v.push_back(1);
    v.push_back(3);

//    vector<int>::iterator it;
    for(auto it = v.begin(); it<v.end(); it++) {
        printf("%d\n", *it);
    }

    sort(v.begin(), v.end());
    for(auto it = v.begin(); it<v.end(); it++) {
        printf("%d\n", *it);
    }
}

int main(void) {
    printf("Problem 17.06\n");
    sortPractice();
    return 0;
}

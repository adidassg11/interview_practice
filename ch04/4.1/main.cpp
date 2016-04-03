#include <stdio.h>
#include <cstdlib> //abs(int)
#include <queue>
#include <map>
#include "BTNode.h"

using namespace std;

#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))


//what if the stack gets too big? there has to be a way of storing as you go
int getHeight(BTNode* node)
{
//    printf("getHeight\n"); 
    if (!node) return 0;
    return 1+MAX(getHeight(node->lchild), getHeight(node->rchild));
}

// returns height but also fills the height map
// should probably put a mutex on this map but whatever
int getHeight2(BTNode* node, map<BTNode*, int> &hMap)
{
//    printf("getHeight2()\n");
    if (!node) return 0;

    if (hMap.find(node) != hMap.end()) return hMap[node];

    if ( !node->lchild && !node->rchild ) {
        hMap[node] = 1;
        return 1;
    }
    else {
        int height = 1 + MAX(getHeight2(node->lchild, hMap), getHeight2(node->rchild, hMap));
        hMap[node] = height;
        return height;
    }
}

void printHMap(map<BTNode*, int> &hMap)
{
    printf("printHMap()\n");
    for (auto it = hMap.begin(); it != hMap.end(); it++) {
        printf("hMap node %p - data: %d height: %d\n", it->first, it->first->data, it->second);
    }
}

bool isBalancedHelper(BTNode* root, map<BTNode*, int> &hMap)
{
    if (!root) return false;

    if (abs(getHeight2(root->lchild, hMap) - getHeight2(root->rchild, hMap)) > 1) {
        return false;
    }

    isBalancedHelper(root->lchild, hMap);
    isBalancedHelper(root->rchild, hMap);

    return true;
}

bool isBalanced(BTNode* root)
{
    printf("isBalanced()\n");

    //going to do a lot of computing heights here, but you could just store in a hash table to save time
    map<BTNode*, int> hMap; //height map
    getHeight2(root, hMap);
    //printHMap(hMap);
        
    return true;
}

int main(void) 
{
    printf("      Problem 4.1        \n");
    printf("= = = = = = = = = = = = =\n");

/*
    BTNode* n1 = new BTNode(5);
    BTNode* n2 = new BTNode(-2, n1, NULL);
    BTNode* t1 = new BTNode(1, new BTNode(2,new BTNode(4),NULL), new BTNode(3,NULL, new BTNode(5, new BTNode(6),NULL)));

    printTreePretty(n1);
    printTreePretty(n2);
    printTreePretty(t1);
    printf("n1 height: %d\n", getHeight(n1));
    printf("n2 height: %d\n", getHeight(n2));
    printf("t1 height: %d\n", getHeight(t1)); //print this for example of how much wasted effort there is
    printf("t1 is balanced? %s\n", isBalanced(t1) ? "yes" : "no");

    delete n1;
    delete n2;
    deleteTree(t1);
*/

    BTNode* t2 = new BTNode(1, new BTNode(2, new BTNode(3, new BTNode(4))), new BTNode(9));
    printTreePretty(t2);
    printf("t2 is balanced? %s\n", isBalanced(t2) ? "yes" : "no");
    deleteTree(t2);
    

/*
    // lame data but works for a bigger example, shows dramatic difference between getHeight() and getHeight2()
    BTNode* t1 = new BTNode(1, new BTNode(2,new BTNode(4),NULL), new BTNode(3,NULL, new BTNode(5, new BTNode(6),NULL)));
    BTNode* t2 = new BTNode(1, new BTNode(2,new BTNode(4),NULL), new BTNode(3,NULL, new BTNode(5, new BTNode(6),NULL)));
    BTNode* t3 = new BTNode(100, t1, t2);
    printTreePretty(t3);
    printf("t1 height: %d\n", getHeight(t3));
    isBalanced(t3);
    deleteTree(t3);
*/

    return 0;
}

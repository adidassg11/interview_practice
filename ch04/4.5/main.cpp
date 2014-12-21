#include <stdio.h>
#include <stack>

#include "helpers.h"
#include "BTNode.h"

using namespace std;


bool isBST(BTNode* btree)
{
    //just do an in-order traversal with a stack
    
    stack<BTNode*> s;
    //makeStackWithNull(btree, s);
    makeStackNoNull(btree, s);
//DEBUG
//    printStack(s);

    int lastInt = INT_MAX;
    while (!s.empty()) {
        BTNode* n = s.top();

printf("n->data: %d lastint: %d\n", n->data, lastInt);
        if (n->data > lastInt) return false; 
        lastInt = n->data;
        s.pop();
    } 
    
    return true;
}


int main(void)
{
    printf("      Problem 4.5        \n");
    printf("= = = = = = = = = = = = =\n");

//easy  BST, but is printing true :(
    BTNode* t1 = new BTNode(2, new BTNode(1), new BTNode(3));
    printTreePretty(t1);
    printf("isBST(t1)? %s\n", isBST(t1) ? "yes" : "no");
    deleteTree(t1);

//should not be BST, but is printing true :(
    BTNode* t2 = new BTNode(1, new BTNode(2, new BTNode(3, new BTNode(4))), new BTNode(9));
    printTreePretty(t2);
    printf("isBST(t2)? %s\n", isBST(t2) ? "yes" : "no");
    deleteTree(t2);

//easy non BST, but is printing true :(
    BTNode* t3 = new BTNode(1, new BTNode(2), new BTNode(3));
    printTreePretty(t3);
    printf("isBST(t3)? %s\n", isBST(t3) ? "yes" : "no");
    deleteTree(t3);

//corner cases  BST, but is printing true :(
    BTNode* t4 = new BTNode(-129084, new BTNode(-2300423), new BTNode(0, NULL, new BTNode(1)));
    printTreePretty(t4);
    printf("isBST(t4)? %s\n", isBST(t4) ? "yes" : "no");
    deleteTree(t4);


    
    return 0;
}

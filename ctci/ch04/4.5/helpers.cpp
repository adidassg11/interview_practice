#include "helpers.h"


void printStack(stack<BTNode*> &s)
{
    printf("Printing stack for %p - ", s.top()); 
    while (!s.empty()) {
        BTNode* n = s.top();
        //print NULL values as 'x'
        //printf("%c ", n ? itoa(n->data) : "x");
        char buf[16];
        snprintf(buf, sizeof(buf), "%d", n->data);
        printf("%s ", n ? buf : "X");
        s.pop(); 
    }

    printf("\n");
}


/*
 This builds up from in-order traversal so rightmost node is on the top of the stack
*/
void makeStackNoNull(BTNode* btree, stack<BTNode*> &s)
{
    BTNode* n = btree;
    //here we aren't even going to bother with children that are NULL
    if (n) {
        if (n->lchild) {
            makeStackNoNull(n->lchild, s);
        }
        s.push(n); //the n check shouldn't actually be necessary
        if (n->rchild) {
            makeStackNoNull(n->rchild, s);
        }
    }
}


// TODO: causes seg fault 11
void makeStackWithNull(BTNode* btree, stack<BTNode*> &s)
{
    BTNode* n = btree;
    if (n) makeStackWithNull(n->lchild, s);
    s.push(n); //here we push n even if it's NULL
    if (n) makeStackWithNull(n->rchild, s);
}


#include <stdio.h>
#include <climits>

struct BTNode
{
    int data;
    BTNode* lchild;
    BTNode* rchild;
    BTNode() { data = INT_MAX; lchild = NULL; rchild = NULL; }
    BTNode(int _data = INT_MAX, BTNode* _lchild = NULL, BTNode* _rchild = NULL): 
                            data(_data),
                            lchild(_lchild), 
                            rchild(_rchild) {}
};

void printBTNode(BTNode* node);
void printTreePretty(BTNode* root);

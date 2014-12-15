#include <stdio.h>
#include <queue>
#include "BTNode.h"

#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))

int getHeight(BTNode* node)
{
    if (!node) return 0;
    return 1+MAX(getHeight(node->lchild), getHeight(node->rchild));
}

bool isBalanced(BTNode* root)
{
    return true;
}

int main(void) 
{
    printf("      Problem 4.1        \n");
    printf("= = = = = = = = = = = = =\n");

    BTNode* n1 = new BTNode(5);
    BTNode* n2 = new BTNode(-2, n1, NULL);
    printTreePretty(n1);
    printTreePretty(n2);
    printf("n1 height: %d\n", getHeight(n1));
    printf("n2 height: %d\n", getHeight(n2));
    delete n1;
    delete n2;

    return 0;
}

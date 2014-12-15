/* this is just to compile BTNode.cpp on its own */

#include <stdio.h>
#include "BTNode.h"

int main(void)
{
    printf("main\n");
    BTNode node(5);
    printBTNode(&node);

    BTNode* tree = new BTNode(1, new BTNode(2, NULL, new BTNode(4)), new BTNode(3));
    printTree(tree);
    printTreePretty(tree);
    deleteTree(tree);
    return 0;
}

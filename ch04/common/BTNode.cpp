#include "BTNode.h"

void printBTNode(BTNode* node)
{
    printf("BTNode data:%d\tmem:%p\tL:%p\tR:%p\n", node->data, node, node->lchild, node->rchild);
}

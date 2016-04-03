#include "node.h"

void printSLL(Node* node) {
    int nodeCtr = 0;
    while (node) {
        printf("Node %d:\n\tAddr: %p\n\tData: %d\n", ++nodeCtr, node, node->data);
        node = node->next;
    }
    return;
}

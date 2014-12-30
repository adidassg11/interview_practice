#include "node.h"

void printNode(Node* node)
{
    if (!node) {
        printf("printNode ERROR, null node\n");
        return;
    }

    printf("Node addr: %p\n\tData: %d\n",  node, node->data);
    return;
}


void printSLL(Node* node) 
{
    int nodeCtr = 0;
    while (node) {
        printf("Node %d:\n\tAddr: %p\n\tData: %d\n", ++nodeCtr, node, node->data);
        node = node->next;
    }
    return;
}

void printSimpleSLL(Node* node)
{
    printf("list: ");
    while (node) {
        printf("%d ", node->data);
        node = node->next;
    }

    printf("\n");
}

void deleteSLL(Node* head)
{
    Node* node = head;
    Node* nextNode = NULL;
    while (node) {
        nextNode = node->next;
        delete node;
        node = nextNode;
    }
}

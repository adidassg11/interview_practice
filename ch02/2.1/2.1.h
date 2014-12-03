#include <stdio.h>
//should be "Node" but whatever
struct node {
    node(int _data, node* _node) : data(_data), next(_node) {}
    int data;
    node* next;
};

void printSLL(node* node);
int removeNextNode(node* node);
bool isDup(node* node1, node* node2);
void removeDupNaive(node* head);


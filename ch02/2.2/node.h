#include <stdio.h>

struct Node {
    Node(int _data, Node* _node) : data(_data), next(_node) {}
    int data;
    Node* next;
};

void printSLL(Node* node);

#include <stdio.h>

struct Node {
    Node(int _data, Node* _node) : data(_data), next(_node) {}
    int data;
    Node* next;
};

void printNode(Node* node);
void printSLL(Node* node);
void printSimpleSLL(Node* node);
void deleteSLL(Node* head);

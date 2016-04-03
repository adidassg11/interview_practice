#include <stdio.h>

//using namespace std;

struct Node {
    int d;
    Node* n;
};

void printN(Node * _n) {
    printf("=Node=\n\tAddr: %p\n\tData: %d\n\tNext: %p\n", _n, _n->d, _n->n);
}

void printSLL(Node * head) {
    Node* curNode = head;
    int numNode = 0;

    while (curNode) {
        printf("Node %d\n", numNode);
        printN(curNode);
        numNode++;
        curNode = curNode->n;
    }
}

//reverse singly linked list
//current then looking forward at next 2
void revSLL1(Node * head) {
    printf("revSLL1\n");

    Node* tmp;
    Node* curNode = head;
    
    if (!curNode) return;

    tmp = curNode->n;
    curNode->n = NULL;
    curNode = tmp;

    while (curNode) {
        tmp = curNode->n;
        curNode->n = curNode;
        curNode = tmp;
    }


    printSLL(curNode);
}

void revSLL2(Node* node) {
    printf("revSLL2\n");

    if (!node) return; //empty list
    if (!node->n) return; //one item list

    Node* cur = node;
    Node* prev = NULL;
    Node* next = node->n;


    int loopCtr = 0;
    while (cur) {
        next = cur->n;
        printf("loop %d\n\tprev: %p\n\tcurr: %p\n\tnext: %p\n", loopCtr, prev, cur, next);
        cur->n = prev;
        prev = cur;
        cur = next;

        loopCtr++;
    }

    node = prev;

    printSLL(node);
}


//probably wrong
Node* revSLL_rec(Node* node) {
    Node* cur = node;
    if (!cur) return NULL;

    Node* rest = revSLL_rec(node->n);
    cur->n = rest;

    printSLL(cur);
    return cur;

}



int main(void){
    Node* head = new Node;
    Node* n1 = new Node;
    Node* n2 = new Node;
    Node* n3 = new Node;
    Node* tail = new Node;

    head->d = 0;
    head->n = n1;

    n1->d = 1;
    n1->n = n2;

    n2->d = 2;
    n2->n = n3;

    n3->d = 3;
    n3->n = tail;

    tail->d = 4;
    tail->n = NULL;

    printf("printSLL(head)\n");
    printSLL(head);

//    revSLL1(head);
    revSLL2(head);
    printSLL(head);

    delete head;
    delete n1;
    delete n2;
    delete n3;
    delete tail;

    return 0;
}

#include <stdio.h>
#include "node.h"

void removeNode(Node* n)
{
    printf("removeNode addr: %p data: %d\n", n, n->data);
    if(!n) return;

    //if next isn't null case
    if(n->next) {
        Node* remNode = n->next;
        n->data = n->next->data;
        n->next = n->next->next;
        delete remNode;
    }
    else{
        delete n;
        n = NULL;
    }
        

    //if next is null case
//TODO
}

int main(void)
{
    printf("in main()\n");
    //create SLL
//    printSLL(); 
    Node* n5 = new Node(5, NULL);
    Node* n4 = new Node(4, n5);
    Node* n3 = new Node(3, n4);
    Node* n2 = new Node(2, n3);
    Node* n1 = new Node(1, n2);
    printSLL(n1);
    removeNode(n5);
    printSLL(n1);
//    delete n5;
    delete n4;
    delete n3;
    delete n2;
    delete n1;
    
    return 0;
}

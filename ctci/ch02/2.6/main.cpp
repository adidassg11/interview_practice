#include <stdio.h>
#include "../common/node.h"

void print10(Node* n)
{
    Node* node = n;
    for (int i = 0; i< 10; i++) {
        printNode(node);
        node = node->next;
    }
}

/*
    Not sure of O() complexity of this
*/
Node* getLoop(Node* n)
{
    if (!n || !n->next) {
        printf("Input ERROR in getLoop()\n");
        return NULL;
    }
    Node* n1 = n;
    Node* n2 = n->next;

    while (n1 != n2) {
        n1 = n1->next->next;
        n2 = n2->next->next->next->next->next;
    }

    printf("found the start of circle in getLoop(): %d\n", n1->data);

    return n1;
}


int main(void)
{
    printf("      Problem 2.6        \n");
    printf("= = = = = = = = = = = = =\n");

    Node* n7 = new Node(7, NULL);
    Node* n6 = new Node(6, n7);
    Node* n5 = new Node(5, n6);
    Node* n4 = new Node(4, n5);
    Node* n3 = new Node(3, n4);
    Node* n2 = new Node(2, n3);
    Node* n1 = new Node(1, n2);
    n7->next = n3;


    Node* list1 = new Node(1, \
                    new Node(2, \
                    new Node(3, NULL)));



//    printSLL(list1);
    getLoop(n1);
    print10(n1);
    printSimpleSLL(list1);
    deleteSLL(list1); 

    return 0;
}

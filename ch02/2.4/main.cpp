#include <stdio.h>
#include "node.h"

//insert second after first
//assumes second used to be before first
void insertNodeAfter(Node* first, Node* second)
{
    Node* lastNode = first->next;
    Node* firstNode = second->next;
    first->next = second;
    second->next = lastNode; 
    firstNode->next = first;
}

/*
LL: 4 3 5 2 -2
x: 3
*/
//returns the head
Node* partitionAroundX(Node* head, int x)
{
    Node* node = head;
    Node* nodeBeforeX = NULL; //won't be accurate until we find X, will server as division point before even finding X
    Node* nodeX = NULL;
    bool foundX = false;
//TODO find x node
    while (node) {
        if (!foundX) {
            if (node->data == x) {
                nodeX = node;
                foundX = true;
            }
            nodeBeforeX = node;
            node = node->next;
        }
        else {
            if (node->data > x) {
                //place node after X 
                insertNodeAfter(nodeX, node);
            }
            node = node->next;
        }

//trying again.., not worrying about the case where X is the beginnin;
    node = head;
    Node* nextNode = node;
    nodeBeforeX = head;
    nodeX = nodeBeforeX->next;
    while (node) {
        nextNode = node->next; //keep track of things in case we move the 'node'
        if (node->data < x) {
            nodeBeforeX = node;
        }
        else {
            insertNodeAfter(nodeX, node);
        }
        node = nextNode;
    }
        
         


//NOTE: remember to keep head corrrect when swapping things around 
        
         
    }
    return head;
}

int main(void)
{
    printf("in main()\n");
    //create SLL
//    printSLL(); 
/*
    Node* n5 = new Node(-2, NULL);
    Node* n4 = new Node(2, n5);
    Node* n3 = new Node(5, n4);
    Node* n2 = new Node(3, n3);
    Node* n1 = new Node(4, n2);
*/
    Node* n5 = new Node(-2, NULL);
    Node* n4 = new Node(2, n5);
    Node* n3 = new Node(5, n4);
    Node* n2 = new Node(3, n3);
    Node* n1 = new Node(4, n2);
    printf("original\n");
    printSLL(n1);
    printf("switched\n");
    insertNodeAfter(Node* first, Node* second)
    
    delete n5;
    delete n4;
    delete n3;
    delete n2;
    delete n1;
    
    return 0;
}

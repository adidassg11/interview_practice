#include <stdio.h>
#include "../common/node.h"

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

Node* addLists(Node* n1, Node* n2)
{
    int carry = 0;
    int total = 0;
    Node* prevNode = NULL;
    Node* newList = NULL;

//TODO: the bug prob has to do with prevNode
    while (n1 || n2) {
        Node* newNode = new Node(0, NULL); 
        if (!newList) newList = newNode;
        prevNode = newNode;
        int n1Val = n1 ? n1->data : 0;
        int n2Val = n2 ? n2->data : 0;
        int newVal = n1Val + n2Val + carry;
        carry = newVal / 10;
        newNode->data = newVal % 10;
        prevNode->next = newNode; 
        n1 = n1 ? n1->next : NULL;
        n2 = n2 ? n2->next : NULL;
    }

    return newList;
}

int main(void)
{
    printf("main\n");
    Node* list1 = new Node(5, \
                    new Node(3, NULL));
    Node* list2 = new Node(1, NULL);
    printSLL(list1);
    printSLL(list2);

//    Node* sumList = addLists(list1, list2);
//    printSLL(sumList);

    deleteSLL(list1); 
    deleteSLL(list2); 
//    deleteSLL(sumList); 

    return 0;
}

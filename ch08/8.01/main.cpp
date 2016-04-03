#include <stdio.h>
#include <memory>
#include <iostream>

using namespace std;

int myglobal = 6;

/* F this
template <typename T>
struct ListNode {
    T data;
    shared_ptr<ListNode<T> > next;
};

typedef ListNode<int> lni;

void printSLL(lni *sll)
{
    ListNode<int> *node = sll;
    while (node != nullptr) {
        cout << node->data << endl;
        node = node->next;
    }
}
*/
struct Node {
    int data;
    Node* next;
};

/*
void printSLL(Node *sll)
{
    Node *node = sll;
    while (node != NULL) {
        cout << node->data << endl;
        node = node->next;
    }
}

Node* mergeSLL(Node *list1, Node *list2)
{
    Node* ret_list = list1->data > list2->data ? list2 : list1;
    printSLL(ret_list);
    return ret_list;
    while (list1 != NULL && list2 != NULL) {
        //asdf
        if (list1->data > list2->data) {
            ret_list->next = list2;
            list2 = list2->next;
        }
        else {
            ret_list->next = list1;
            list1 = list1->next;
        }
    }

    // Now carry out the rest of the whichever list has something left over
    ret_list->next = list1 ? list1 : list2;
    return ret_list;
}

*/

int main(void)
{
    printf("hello\n");
    Node *n1 = new Node();
    /*
    Node *n2 = new Node();
    Node *n3 = new Node();
    Node *n4 = new Node();
    Node *n5 = new Node();
    Node *n6 = new Node();
    n1->data = 1; //head
    n1->next = n2;
    n2->data = 2;
    n2->next = n4;
    n3->data = 3;
    n3->next = n5; //head
    n4->data = 4;
    n4->next = NULL;
    n5->data = 5;
    n5->next = n6;
    n6->data = 6;
    n6->next = NULL;
    */

    //printSLL(n1);
    //printSLL(n3);
   // printSLL(mergeSLL(n1, n3));
    delete n1;
    /*
    delete n2;
    delete n3;
    delete n4;
    delete n5;
    delete n6;
    */
    cout << "hello";
    return 0;
}

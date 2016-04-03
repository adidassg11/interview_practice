#include "2.1.h"

//using namespace std;

/* questions to ask:
- duplicates means data, right? what if it's pointer or something?
- what's the temp buffer mean?
- remove any duplicate? or everything after the first?
*/

void printSLL(node* node) {
    int nodeCtr = 0;
    while (node) {
        printf("Node %d:\n\tAddr: %p\n\tData: %d\n", nodeCtr, node, node->data);
        node = node->next;
    }
    return;
}

//only valid if node and next node exist
int removeNextNode(node* node) {
    if (!node) return -1;
    if (!node->next) return -1;
    
    node->next = node->next->next; 
    delete node->next;
    return 0;
}

bool isDup(node* node1, node* node2) {
    if (!node1 || !node2) return false;
    return (node1->data == node2->data); 
}

//this just walks thru in O(n2) time comparing everything, no storage
void removeDupNaive(node* head) {
    node* node = head;
    while (node) {
        //duplicate candidate
        node* dupCand = head->next;
        while (dupCand) {
            if isDup(node, dupCand) {
                node* nextNextNode = dupCand->next;
                removeNextNode(node);
                node->next = nextNextNode;
                dupCand = nextNextNode;
            }
            else {
                dupCand = dupCand->next;
            }
        }
        node = node->next;
    }
    return;
}

int main(void) {
    node* n3 = new node(2, NULL);
    node* n2 = new node(1, n3);
    node* n1 = new node(1, n2);
    node* n0 = new node(0, n1);

    printSLL(n0); 

    delete n0;
    delete n1;
    delete n2;
    delete n3;

    return 0;
}

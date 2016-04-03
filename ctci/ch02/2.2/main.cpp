#include <stdio.h>
#include <cstdlib> //exit()
#include <stack>
#include "node.h"

using namespace std;

/*
    this uses O(n) space and O(n+k) time, we can do better
*/
int findKthToLast(Node* n, int k)
{
    if (k<1) {
        printf("ERROR, k too small\n");
        return(-1);
    }

    if (!n) {
        printf("ERROR, node is NULL\n");
        return(-1);
    }
        

    stack<Node*> stack;
    Node* nextNode = n;
    int numNodes = 0;

    while (nextNode) {
        stack.push(nextNode); 
        nextNode = nextNode->next;
        numNodes++;
    }

    if (k>numNodes) {
        printf("ERROR, k too large\n");
        return(-1);
    }

    Node* retNode = n;

    for (int i = k-1; i>0; i--) {
        stack.pop();
    }

    retNode = stack.top();
    
    printf("retNode: %p val: %d\n", retNode, retNode->data);

    return retNode->data;
}

/*
    sneaky but easy technique to find in O(n) and constant mem, just use two counters
*/
int findKthToLast2(Node* n, int k)
{
    if ( (!n) || (k<1) ) {
        printf("args error in findKthToLast2()\n");
        return -1;;
    }
    Node* nl = n; //leader node
    Node* nf = n; //follower node, will end up as target node k

    while (k>0) {
        if (!nl) {
            printf("not enough nodes\n");
            return -1;
        }
        nl = nl->next;
        k--;
    }

    while (nl) {
        nl = nl->next;
        nf = nf->next;
    }

    printf("retNode: %p val: %d\n", nf, nf->data);
    return nf->data;
}


int main(void)
{
    printf("in main\n");

    //create SLL
    Node* n5 = new Node(5, NULL);
    Node* n4 = new Node(4, n5);
    Node* n3 = new Node(3, n4);
    Node* n2 = new Node(2, n3);
    Node* n1 = new Node(1, n2);
    printSLL(n1);
    /*
    findKthToLast(n1, 1);
    findKthToLast(n1, 5);
    findKthToLast(n1, 2);
    findKthToLast(n1, 0);
    findKthToLast(n1, 6);
    */
    findKthToLast2(n1, 1);
    findKthToLast2(n1, 5);
    findKthToLast2(n1, 2);
    findKthToLast2(n1, 0);
    findKthToLast2(n1, 6);
    delete n5;
    delete n4;
    delete n3;
    delete n2;
    delete n1;


    return 0;
}

#include <stdio.h>
#include "BTNode.h"

/*
example:
need to keep cutting the array in half

                     lchild  root rchild
                        v     v     v
    int[10] arr = {0,1, 2, 3, 4,5,6,7,8,9};
*/
BTNode* createTree(int arr[], int size)
{
    //can work recursively storing node into the middle of the array

    BTNode* node = new BTNode(arr[0]);
    return node;
}

int main(void)
{
    printf("      Problem 4.3        \n");
    printf("= = = = = = = = = = = = =\n");

    int arr[10]= {0,1, 2, 3, 4,5,6,7,8,9};
    BTNode* bTree = createTree(arr, 10);
    deleteTree(bTree);
    return 0;
}

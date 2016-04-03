#include <stdio.h>
#include <queue>
#include "helpers.h"
#include "BTNode.h"


using namespace std;

/* return structure looks like this
ret
v
rn
v
rn->rn
v
rn->rn->rn

*/

//tNode is tree node
RowNode* createRows(BTNode* tNode)
{
    //use a queue with special node that separates levels
    // can we do this without a queue?
    //don't worry about NULL nodes

    queue<BTNode*> q;
    q.push(tNode);

    //load up the queue then empty it, or build the LL all in one try?
    
//TODO: this is the main algo
    while (!q.empty()) {
        BTNode* btn = q.front();
        q.pop();
        if (btn) {
            if (btn->data == LEVEL_SEPARATOR) {
    //TODO this isn't correct
                continue; 

            }
            else {
                q.push(btn->lchild);
                q.push(btn->rchild);
            }
        }
        
    }

    RowNode* rn = NULL;
    
    return rn;
}


int main(void)
{
    printf("      Problem 4.4        \n");
    printf("= = = = = = = = = = = = =\n");

    //row list
/*
1
2 3
4 5
*/
/*
    RowNode* rList = new RowNode(1, NULL,
                    new RowNode(2, new RowNode(3, NULL, NULL), 
                    new RowNode(4, new RowNode(5, NULL, NULL), 
                         NULL)));
//    printRowSimple(rList);
    printAllLevels(rList);
    deleteAllNodes(rList);
*/
    BTNode* t2 = new BTNode(1, new BTNode(2, new BTNode(3, new BTNode(4))), new BTNode(9));
    printTreePretty(t2);
    RowNode* rn = createRows(t2);
    printAllLevels(rn); 
    deleteTree(t2);
    deleteAllNodes(rn); 

    return 0;
}

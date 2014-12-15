#include <stdio.h>
#include <queue>
#include <stdlib.h> //exit()
#include "BTNode.h"

using namespace std;

inline void printXSpaces(int x)
{
/*
    for (int i = 0; i<x; i++) {
        printf(".");
    }
    */
}

void printBTNode(BTNode* node)
{
    printf("BTNode data:%d\tmem:%p\tL:%p\tR:%p\n", node->data, node, node->lchild, node->rchild);
}

void printTree(BTNode* root)
{
    if (!root) {
        printf("printTree() empty root\n");
        exit(EXIT_FAILURE);
    }

    //using INT_MAX as level separator 
    printf("max: %d\n", INT_MAX);
    printf("sep: %d\n", LEVEL_SEPARATOR);

    //just going to use full nodes instead of pointers
    // makes NULL nodes easier
    queue<BTNode*> q;
    q.push(root);
    
    while (!q.empty()) {
        BTNode* lNode = NULL;
        BTNode* rNode = NULL;

        if (!q.empty()) {
            lNode = q.front(); 
            q.pop();
        }
        if (!q.empty()) {
            rNode = q.front(); 
            q.pop();
        }
        
        if (lNode) {
            printf(" %d ", lNode->data);
            if (lNode->lchild) {
                q.push(lNode->lchild);
            }
            if (lNode->rchild) {
                q.push(lNode->rchild);
            }
        }

        if (rNode) {
            printf(" %d ", rNode->data);
            if (rNode->lchild) {
                q.push(rNode->lchild);
            }
            if (rNode->rchild) {
                q.push(rNode->rchild);
            }
        }
    }
    printf("\n");
}

void printTreePretty(BTNode* root)
{
    if (!root) {
        printf("printTreePretty() empty tree\n");
        exit(EXIT_FAILURE);
    }

    //these are important for spacing
    int levels = getNumLevels(root);
    int curLevel = 1;

    queue<BTNode*> q;
    q.push(root);
    q.push(new BTNode(LEVEL_SEPARATOR));
    
    printXSpaces((1<<(levels-curLevel))-1);
    
    while (!q.empty()) {
        BTNode* n = q.front();
        q.pop();
        if (n) {
            if (n->data != LEVEL_SEPARATOR) {
                q.push(n->lchild);
                q.push(n->rchild);
                printf("%d", n->data);
                printXSpaces((1<<(levels-curLevel))-1);
            }
            else {
                if(!q.empty()) {
                    q.push(new BTNode(LEVEL_SEPARATOR));
                }
                printXSpaces((1<<(levels-curLevel))-1);
                printf("\n");
                curLevel++;
                if (curLevel < levels) {
                    printXSpaces((1<<(levels-curLevel))-1);
                }
                delete n;
            }
        }
        else {
            printf("x");
        } 
    }
}

//might be junk
void parseTreeThruQ(BTNode* root, int &levels)
{
    queue<BTNode*> q;
    q.push(root);
    q.push(new BTNode(LEVEL_SEPARATOR));
    
    while (!q.empty()) {
        BTNode* n = q.front();
        q.pop();
        if (n) {
            if (n->data != LEVEL_SEPARATOR) {
                q.push(n->lchild);
                q.push(n->rchild);
                printf(" %d", n->data);
            }
            else {
                if(!q.empty()) {
                    q.push(new BTNode(LEVEL_SEPARATOR));
                }
                printf("\n");
                levels++;
                delete n;
            }
        }
        else {
            printf(" x");
        } 
    }
}


void deleteTree(BTNode* root)
{
    printf("deleting the following nodes: ");
    //just q up all the nodes then delete them
    queue<BTNode*> q;
    q.push(root);
     
    while(!q.empty()) {
        BTNode* n = q.front();
        q.pop();

        if (n) {
            if (n->lchild) q.push(n->lchild); 
            if (n->rchild) q.push(n->rchild); 
            printf(" %d", n->data);
            delete n;
        }

    }

    printf("\n");
}

int getNumLevels(BTNode* root) 
{
    int levels = 0;
    queue<BTNode*> q;
    q.push(root);
    q.push(new BTNode(LEVEL_SEPARATOR));

    while (!q.empty()) {
        BTNode* n = q.front();
        q.pop();
        if (n) {
            if (n->data == LEVEL_SEPARATOR) {
                levels++;
                if (q.empty()) {
                    //all done, wrap up
                    delete n;
                }
                else {
                    q.push(n);
                    
                }
            }
            else {
                q.push(n->lchild);
                q.push(n->rchild);
            }
        } 
    }

    printf("getNumLevels(): %d\n", levels);
    return levels;
}

#include <climits>

#define INVALID_DATA INT_MAX
#define LEVEL_SEPARATOR (INT_MAX -1)

struct BTNode
{
    int data;
    BTNode* lchild;
    BTNode* rchild;
    BTNode() { data = INT_MAX; lchild = NULL; rchild = NULL; }
    BTNode(int _data = INT_MAX, BTNode* _lchild = NULL, BTNode* _rchild = NULL): 
                            data(_data),
                            lchild(_lchild), 
                            rchild(_rchild) {}
};

void printBTNode(BTNode* node);
void printTree(BTNode* root);
void printTreePretty(BTNode* root);
void deleteTree(BTNode* root);
void parseTreeThruQ(BTNode* root, int &levels);


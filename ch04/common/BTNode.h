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

inline void printXSpaces(int x);
void printBTNode(BTNode* node);
void printTree(BTNode* root);
void printTreePretty(BTNode* root);
void deleteTree(BTNode* root);
void parseTreeThruQ(BTNode* root, int &levels);
int getNumLevels(BTNode* root);

/* scratch
2levels:
12.45
1.3.5

or

1.3
.2.

3 levels:
1234.6789
12.456.89
1.3.5.7.9

or
123.567
1.345.7
.2.4.6.


*/

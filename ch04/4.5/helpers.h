#ifndef _4_5_HELPERS
#define _4_5_HELPERS

#include <stack>
#include <stdio.h>
#include <stdlib.h> //exit, itoa

#include "BTNode.h"

using namespace std;

void printStack(stack<BTNode*> &s);
void makeStackNoNull(BTNode* btree, stack<BTNode*> &s);
void makeStackWithNull(BTNode* btree, stack<BTNode*> &s);

#endif // _4_5_HELPERS 

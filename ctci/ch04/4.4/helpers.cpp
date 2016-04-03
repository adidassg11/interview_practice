#include "helpers.h"

#include <stdio.h>

void printRowDetailed(RowNode* node) {
    int nodeCtr = 0;
    while (node) {
        printf("RowNode %d:\n\tAddr: %p\n\tData: %d\n", ++nodeCtr, node, node->data);
        node = node->next;
    }
    return;
}

void printRowSimple(RowNode* node, int rowNum) {
    printf("Row %d - ", rowNum);
    while (node) {
        printf(" %d", node->data);
        node = node->next;
    }
    printf("\n");
}

void printAllLevels(RowNode* node)
{
    int levelNum = 0;
    while (node) {
        RowNode* nextRow = node->nextLevel;
        printRowSimple(node, levelNum++);
        node = nextRow;
    }
}

void deleteRowNodes(RowNode* node)
{
    while (node) {
        RowNode* nextNode = node->next;
        delete node;
        node = nextNode;    
    } 
}

void deleteAllNodes(RowNode* node)
{
    while (node) {
        RowNode* nextLevel = node->nextLevel;
        deleteRowNodes(node);
        node = nextLevel;
    }
}


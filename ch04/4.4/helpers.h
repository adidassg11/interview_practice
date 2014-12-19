
//idk  why i added 'row' to this, oh well
struct RowNode {
    RowNode(int _data, RowNode* _node, RowNode* _nextLevelNode) : data(_data), 
                                                                next(_node), 
                                                                nextLevel(_nextLevelNode) {}
    int data;
    RowNode* next;
    RowNode* nextLevel;
};

struct LevelNode {
    LevelNode(int _data, LevelNode* _levelNode, RowNode* _rowNode) : data(_data), 
                                                            nextLevel(_levelNode),   
                                                            row(_rowNode) {}
    int data;
    LevelNode* nextLevel;
    RowNode* row;
};
void printRowDetailed(RowNode* node);
void printRowSimple(RowNode* node, int rowNum);
void printAllLevels(RowNode* node);
void deleteRowNodes(RowNode* node);
void deleteAllNodes(RowNode* node);

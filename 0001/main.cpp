#include <stdio.h>
#include <list>
#include <string>
#include <vector>

using namespace std;


struct Node {
    Node(int val) : d(val) {}
    int d; //data
    Node* l; //left child
    Node* r;
};

void printTreeHelper(Node* n, vector<string>& tree, int depth);

void printTree(Node* n) {
    vector<string> tree;
    string s = "";
    tree.push_back(s);
    printTreeHelper(n, tree, 0);

    for(int i=0; i<tree.size(); i++) {
        printf("tree: %s\n", tree[i].c_str());
    }
    
}

void printTreeHelper(Node* n, vector<string>& tree, int depth) {
    if(!n) return;
//DEBUG
    printf("in helper with depth %d\n", depth);

    

    tree[depth] += " ";
    tree[depth] += n->d;

    printf("data: %d\n", n->d);

    printTreeHelper(n->l, tree, depth+1); 
    printTreeHelper(n->r, tree, depth+1); 

}


int main(void) {
    printf("in main\n");

//    Node* n4 = new Node(4);
    Node* n2 = new Node(2);
    Node* n1 = new Node(1);
    Node* n3 = new Node(3);

    n1->l = NULL;
    n1->r = NULL;

    n2->l = n1;
    n2->r = n3;
    
    n3->l = NULL;
    n3->r = NULL;

    printTree(n2);

    delete n1;
    delete n2;
    delete n3;
//    delete n4;

    return 0;
}

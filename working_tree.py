#include <bits/stdc++.h>
using namespace std;

/* A binary tree node has data, pointer to left child
and a pointer to right child */
class Node:
    def __init__(self, data, left=None, right=None):
    self.data = data;
    self.left = left;
    self.right = right;

struct Node* newNode(char data)
{
    struct Node* node = new Node;
    node->data = data;
    node->left = node->right = NULL;
    return (node);
}

# /* Recursive function to construct binary of size
# len from Inorder traversal in[] and Preorder traversal
# pre[]. Initial values of inStrt and inEnd should be
# 0 and len -1. The function doesn't do any error
# checking for cases where inorder and preorder
# do not form a tree */
def build_tree(infix, prefix):
    prefix_index = 0
    current = prefix[prefix_index]


struct Node* buildTree(string in, string pre, int inStrt, int inEnd, unordered_map<char, int> &mp)
{
    static int preIndex = 0;

    if (inStrt > inEnd)
        return NULL;

    /* Pick current node from Preorder traversal using preIndex
    and increment preIndex */
    int curr = pre[preIndex++];
    struct Node* tNode = newNode(curr);

    /* If this node has no children then return */
    if (inStrt == inEnd)
        return tNode;

    /* Else find the index of this node in Inorder traversal */
    int inIndex = mp[curr];

    /* Using index in Inorder traversal, construct left and
    right subtress */
    tNode->left = buildTree(in, pre, inStrt, inIndex - 1, mp);
    tNode->right = buildTree(in, pre, inIndex + 1, inEnd, mp);

    return tNode;
}

// This function mainly creates an unordered_map, then
// calls buildTree()
struct Node* buldTreeWrap(string in, string pre, int len)
{
    // Store indexes of all items so that we
    // we can quickly find later
    unordered_map<char, int> mp;
    for (int i = 0; i < len; i++)
 {
  mp[in[i]] = i;
 }

    return buildTree(in, pre, 0, len - 1, mp);
}

/* This funtcion is here just to test buildTree() */
void printInorder(struct Node* node)
{
    if (node == NULL)
        return;
    printInorder(node->left);
    printf("%c ", node->data);
    printInorder(node->right);
}

int main(int argc, char *argv[])
{
 string infix, prefix;
 while(cin >> infix >> prefix){
  cout << "infix: "<< infix << endl;
  struct Node* root = buldTreeWrap(prefix, infix, infix.size());
  printInorder(root);
 }
 return 0;
}

/*
 * 2265. Count Nodes Equal to Average of Subtree
 * 
 * Given the `root` of a binary tree, return the number of nodes where the value
 * of the node is equal to the average of the values in its subtree.
 * 
 * Note:
 *     The average of `n` elements is the sum of the `n` elements divided by `n`
 *         and rounded down to the nearest integer.
 *     A subtree of `root` is a tree consisting of `root` and all of its
 *         descendants.
 */

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int answer;

typedef struct {
    int population;
    int total;
} DFS_Result;  /* name of struct type goes at end b/c of `typedef` */

DFS_Result dfs(struct TreeNode* root) {  /* `TreeNode` isn't typedef'ed */
    if (root == NULL) {
        DFS_Result result;
        result.population = 0;  /* `result` isn't a pointer, so `->` is invalid */
        result.total = 0;
        return result;
    }

    DFS_Result left  = dfs(root->left);
    DFS_Result right = dfs(root->right);

    DFS_Result result;
    result.population = 1 + left.population + right.population;
    result.total = root->val + left.total + right.total;

    if (result.total / result.population == root->val) {
        answer++;
    }

    return result;
}

int averageOfSubtree(struct TreeNode* root) {
    /* O(n) time, O(n) space solution */
    answer = 0;  /* global variable is mutated by `dfs()` call */
    dfs(root);
    return answer;
}
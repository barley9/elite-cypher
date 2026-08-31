/*
 * 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
 * 
 * A critical point in a linked list is defined as either a local maxima or a
 * local minima.
 * 
 * A node is a local maxima if the current node has a value strictly greater than
 * the previous node and the next node.
 * 
 * A node is a local minima if the current node has a value strictly smaller than
 * the previous node and the next node.
 * 
 * Note that a node can only be a local maxima/minima if there exists both a
 * previous node and a next node.
 * 
 * Given a linked list `head`, return an array of length 2 containing
 * `[minDistance, maxDistance]` where `minDistance` is the minimum distance
 * between any two distinct critical points and `maxDistance` is the maximum
 * distance between any two distinct critical points. If there are fewer than two
 * critical points, return `[-1, -1]`.
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* nodesBetweenCriticalPoints(struct ListNode* head, int* returnSize) {
    if ((head == NULL) | (head->next == NULL) | (head->next->next == NULL)) {
        int* result = malloc(2 * sizeof(int));
        result[0] = result[1] = -1;
        *returnSize = 2;
        return result;
    }

    /* TODO: everything else */

    *returnSize = 0;
    return NULL;
}
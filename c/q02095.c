/*
 * 2095. Delete the Middle Node of a Linked List
 * 
 * You are given the `head` of a linked list. Delete the middle node, and return
 * the `head` of the modified linked list.
 * 
 * The middle node of a linked list of size `n` is the `floor(n / 2)`th node from
 * the start using 0-based indexing, where `floor(x)` denotes the largest integer
 * less than or equal to `x`. E.g. for `n` = `1`, `2`, `3`, `4`, and `5`, the
 * middle nodes are `0`, `1`, `1`, `2`, and `2`, respectively.
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteMiddle(struct ListNode* head) {
    if ((head == NULL) || (head->next == NULL)) {
        return NULL;
    }

    /* Locate middle node */
    struct ListNode* slow = head;
    struct ListNode* fast = head->next;
    while ((fast->next != NULL) && (fast->next->next != NULL)) {
        slow = slow->next;
        fast = fast->next->next;
    }

    /* Delete middle node */
    struct ListNode* temp = slow->next;
    slow->next = slow->next->next;
    free(temp);

    return head;
}
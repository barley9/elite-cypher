/*
 * 61. Rotate List
 * 
 * Given the `head` of a linked list, rotate the list to the right by `k`
 * places.
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* rotateRight(struct ListNode* head, int k) {
    /* O(2n) time, O(1) space solution */

    /* If LL is empty, or has size 1, or rotated by 0 places, return LL unchanged */
    if ((head == NULL) || (head->next == NULL) || (k == 0)) {
        return head;
    }

    /* Locate tail node and compute LL length (first pass) */
    struct ListNode* tail = head;
    int ll_len = 1;
    while (tail->next != NULL) {
        tail = tail->next;
        ll_len++;
    }

    /* Locate node after which to cut LL (second pass) */
    struct ListNode* cut_after = head;
    for (int i = 0; i < ll_len - (k % ll_len) - 1; i++) {
        cut_after = cut_after->next;
    }

    /* Stitch LL pieces back together */
    tail->next = head;
    head = cut_after->next;
    cut_after->next = NULL;

    return head;
}
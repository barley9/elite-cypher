/*
 * 3517. Smallest Palindromic Rearrangement I
 * 
 * You are given a palindromic string `s`.
 * 
 * Return the lexicographically smallest palindromic permutation of `s`.
 */

void bubblesort(char* arr, int size) {
    bool done = false;
    while (!done) {
        done = true;
        for (int i = 1; i < size; i++) {
            if (arr[i - 1] > arr[i]) {
                char temp = arr[i];
                arr[i] = arr[i - 1];
                arr[i - 1] = temp;
                done = false;
            }
        }
    }
}

char* smallestPalindrome(char* s) {
    /*
     * TOO SLOW
     * O(n^2) time, O(1) space solution
     */
    /* Compute length of `s` */
    char* end = s;
    while (*end != '\0') {
        end++;
    }
    int len = (int) (end - s);

    char middle;
    if (len % 2 == 1) {
        middle = s[len / 2];
    } else {
        middle = '\0';
    }

    bubblesort(s, len / 2);
    for (int i = 0; i < len / 2; i++) {
        s[len - i - 1] = s[i];
    }
    if (middle != '\0') {
        s[len / 2] = middle;
    }

    return s;
}
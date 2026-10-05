/*
 * 856. Score of Parentheses
 * 
 * Given a balanced parentheses string `s`, return the score of the string.
 * 
 * The score of a balanced parentheses string is based on the following rule:
 *     "()" has score `1`.
 *     `AB` has score `A + B`, where `A` and `B` are balanced parentheses strings.
 *     `(A)` has score `2 * A`, where `A` is a balanced parentheses string.
 */

int scoreOfParentheses(char* s) {
    /* O(n) time, O(n) space solution */
    int stack[64];  /* we know len(s) <= 50 */
    int* top = stack;  /* pointer to first empty cell on stack */

    for (char* c = s; *c != '\0'; c++) {
        if (*c == '(') {
            *top = -1;  /* represent left-paren with -1 */
            top++;
        } else {
            /* Add up everything inside pair of parens */
            int total = 0;
            while (*(top - 1) != -1) {
                total = total + *(--top);
            }
            top--;

            /* If nothing inside, push `1`; else, push double */
            if (total == 0) {
                *top = 1;
            } else {
                *top = 2 * total;
            }
            top++;
        }
    }

    /* Sum up everything remaining on `stack` */
    int result = 0;
    while (top > stack) {
        result = result + *(--top);
    }
    return result;
}
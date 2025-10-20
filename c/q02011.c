/*
 * 2011. Final Value of Variable After Performing Operations
 *
 * There is a programming language with only four operations and one variable
 * `X`:
 *     `++X` and `X++` increments the value of the variable `X` by `1`.
 *     `--X` and `X--` decrements the value of the variable `X` by `1`.
 * 
 * Initially, the value of `X` is `0`.
 * 
 * Given an array of strings `operations` containing a list of operations,
 * return the final value of `X` after performing all the operations.
 */

int finalValueAfterOperations(char** operations, int operationsSize) {
    /* O(n) time, O(1) space solution */
    int result = 0;
    
    for (int i = 0; i < operationsSize; i++) {
        for (int j = 0; j < strlen(operations[i]); j++) {
            if (operations[i][j] == 43) {  /* ASCII '+' = 43 */
                result++;
                break;
            } else {
                if (operations[i][j] == 45) {  /* ASCII '-' = 45 */
                    result--;
                    break;
                }
            }
        }
    }

    return result;
}
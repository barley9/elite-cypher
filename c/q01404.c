/*
 * 1404. Number of Steps to Reduce a Number in Binary Representation to One
 * 
 * Given the binary representation of an integer as a string `s`, return the
 * number of steps to reduce it to `1` under the following rules:
 *     If the current number is even, you have to divide it by `2`.
 *     If the current number is odd, you have to add `1` to it.
 * 
 * It is guaranteed that you can always reach `1` for all test cases.
 */

/* WRONG; integer overflow */
unsigned long long int char_to_int(char* s) {
    /* Converts `char` array to `int`. If  */
    unsigned long long int result = 0;
    
    for (int i = 0; i < strlen(s); s++) {
        result = result << 1;
        
        if (s[i] == '1') {
            result = result | 1;
        }
    }

    return result;
}

int numSteps_OLD(char* s) {
    /*
     * O(2 * strlen(s)) time, O(1) space solution.
     * WRONG: integer overflow; not all testcases fit in 64-bit
     * `unsigned long long int`.
     */
    unsigned long long int n = char_to_int(s);

    printf("%llu\n", n);
    
    int count = 0;
    while (n > 1) {
        if (n & 1) {
            n = (n + 1) >> 1;
            count = count + 2;
        } else {
            n = n >> 1;
            count++;
        }
    }

    return count;
}


/* Attempt #2; UNFINISHED */
int numSteps(char* s) {
    /* Allocate adequate buffer for `s` */
    int BUFFER_SIZE = 256;
    char* buffer[BUFFER_SIZE] = {0};
    int i = 0;
    for (int i = 0; i < strlen(s); i++) {
        buffer[BUFFER_SIZE - strlen(s) + i] = s[i];
    }

    /* Seek to end of `s` */
    char* digit = s;
    while (*(digit + 1) != '\0') {  /* assume `s` is null-terminated */
        printf("%s,", digit);
        digit++;
    }
    printf("INFO: Final digit of `s`: %c\n", *digit);

    unsigned int count = 0;
    while (digit > s) {
        if (*digit == '1') {
            /* add 1 to `n`, carrying if necessary */
            *digit = '0';
            char* carry = digit;
            while (*carry == '1') {
                carry--;
            }
            if (carry < s) {
                printf("WARNING: Overflow in addition '1 + %s'\n", s);
            }
            *carry = '0';
        } else {
            /* divide by 2, left-shifting by 1 */
            digit--;
        }
        count++;
    }
    return count;
}
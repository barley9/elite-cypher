/*
 * 1967. Number of Strings That Appear as Substrings in Word
 * 
 * Given an array of strings `patterns` and a string `word`, return the number of
 * strings in `patterns` that exist as a substring in `word`.
 * 
 * A substring is a contiguous sequence of characters within a string.
 */

bool OLD1_contains_substring(char* str, char* sub) {
    /*
     * Takes two null-terminated strings. Returns true if `sub` is a substring
     * of `str`
     */
    printf("\tsearching for '%s' in '%s'...\n", sub, str);
    char* c = str;
    char* d = sub;
    while (*c != '\0') {
        if (*c == *d) {
            printf("\tmatched '%c' at position %i; continuing\n", *d, (int) (c - str));
            d++;  /* check next char in `sub` */
            if (*d == '\0') {
                return true;  /* reached end of `sub`; all chars matched */
            }
        } else {
            printf("\tfailed to match '%c' at position %i; restarting\n", *d, (int) (c - str));
            d = sub;  /* restart match */
        }
        c++;
    }

    return false;
}

bool OLD2_contains_substring(char* str, char* sub) {
    /*
     * Takes two null-terminated strings. Returns true if `sub` is a substring
     * of `str`
     */
    char* c = str;
    char* d = sub;

    printf("finding '%s' in '%s'...\n", sub, str);

    while (*c != '\0') {
        if (*d == *c) {
            printf("\tmatched '%c' at position %i; continuing\n", *d, (int) (c - str));
            /* if match, check next char */
            d++;
            c++;
            if (*d == '\0') {
                return true;  /* if reached end of `sub`, exact match found */
            }
        } else {
            printf("\tfailed to match '%c' at position %i; ", *d, (int) (c - str));
            /* if not match, restart `d` and check again; if already restarted, move on */
            if (d > sub) {
                printf("restarting\n");
                d = sub;  /* restart `d` */
            } else {
                printf("moving on\n");
                c++;  /* move on */
            }
        }
    }

    return false;
}

bool contains_substring(char* str, char* sub) {
    char* c = str;
    while (*c != '\0') {
        /* restart at every index in `str` */
        int i = 0;
        char* d = sub;
        while (*(c + i) != '\0') {
            if (*(c + i) == *d) {
                i++;
                d++;
                if (*d == '\0') {
                    return true;
                }
            } else {
                break;
            }
        }
        c++;
    }

    return false;
}

int numOfStrings(char** patterns, int patternsSize, char* word) {
    /* O(m*n) time, O(1) space solution */
    int total = 0;
    for (int i = 0; i < patternsSize; i++) {
        if (contains_substring(word, patterns[i])) {
            total++;
        }
    }
    return total;
}
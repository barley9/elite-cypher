/*
 * 3120. Count the Number of Special Characters I
 * 
 * You are given a string `word`. A letter is called special if it appears both in
 * lowercase and uppercase in `word`.
 * 
 * Return the number of special letters in `word`.
 */

int numberOfSpecialChars(char* word) {
    /* O(n) time, O(1) space solution */
    int* letters[128] = {0};  /* use ASCII to index into letters */

    while (*word) {  /* while char referenced by `word` ptr is not null... */
        /* printf("%i -> %c\n", word, *word); */
        letters[*word] += 1;
        word++;
    }

    int total = 0;
    for (int i = 'A'; i < 'Z' + 1; i++) {
        total = total + ((letters[i] > 0) && (letters[i + 32] > 0));
    }

    return total;
}
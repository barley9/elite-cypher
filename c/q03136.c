/*
 * 3136. Valid Word
 * 
 * A word is considered valid if:
 *     It contains a minimum of 3 characters.
 *     It contains only digits (0-9), and English letters (uppercase and lowercase).
 *     It includes at least one vowel.
 *     It includes at least one consonant.
 * 
 * You are given a string `word`.
 * 
 * Return `true` if `word` is valid, otherwise, return `false`.
 * 
 * Notes:
 *     'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
 *     A consonant is an English letter that is not a vowel.
 */


bool isvowel(char c) {
    /* https://stackoverflow.com/a/60584910/19528166 */
    switch(tolower(c)) {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
            return true;
        default:
            return false;
    }
}

bool isValid(char* word) {
    /* O(n) time, O(1) space solution */
    bool v = false;  /* `word` contains at least one vowel */
    bool c = false;  /* `word` contains at least one consonant */

    int i = 0;  /* need to access `i` outside loop */
    for (; word[i] != 0; i++) {
        if (isvowel(word[i])) {
            v = true;
        } else {
            if ((65 <= word[i] && word[i] <= 90) || (97 <= word[i] && word[i] <= 122)) {
                c = true;
            } else {
                if (!(48 <= word[i] && word[i] <= 57)) {
                    return false;
                }
            }
        }
    }
    return (i >= 3) && v && c;
}
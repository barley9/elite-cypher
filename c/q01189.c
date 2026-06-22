/*
 * 1189. Maximum Number of Balloons
 * 
 * Given a string `text`, you want to use the characters of `text` to form as many
 * instances of the word "balloon" as possible.
 * 
 * You can use each character in `text` at most once. Return the maximum number of
 * instances that can be formed.
 */

int maxNumberOfBalloons(char* text) {
    /* O(n) time, O(1) space solution */
    int counts[128] = {0};  /* allocate sufficient space for lowercase ASCII */
    
    char* c = text;
    while (*c != '\0') {
        counts[*c]++;
        c++;
    }

    int minimum = 10000;  /* there's probably a better way to do this... */
    if (counts['b']     < minimum) minimum = counts['b']    ;
    if (counts['a']     < minimum) minimum = counts['a']    ;
    if (counts['l'] / 2 < minimum) minimum = counts['l'] / 2;
    if (counts['o'] / 2 < minimum) minimum = counts['o'] / 2;
    if (counts['n']     < minimum) minimum = counts['n']    ;

    return minimum;
}
/*
 * 717. 1-bit and 2-bit Characters
 * 
 * We have two special characters:
 *     The first character can be represented by one bit `0`.
 *     The second character can be represented by two bits (`10` or `11`).
 * 
 * Given a binary array `bits` that ends with `0`, return `true` if the last
 * character must be a one-bit character.
 */

bool isOneBitCharacter(int* bits, int bitsSize) {
    /* O(n) time, O(1) space solution */
    int state = 0;
    
    for (int i = 0; i < bitsSize; i++) {
        if (state) {
            state = 0;
        } else {
            if (bits[i]) {
                state = 1;
            } else {
                if (i == bitsSize - 1) {
                    return true;
                }
            }
        }
    }

    return false;
}
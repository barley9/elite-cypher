/**
 * 1550. Three Consecutive Odds
 *
 * Given an integer array arr, return true if there are three consecutive odd
 * numbers in the array. Otherwise, return false. 
 **/

bool threeConsecutiveOdds(int* arr, int arrSize) {
    int count = 0;
    for (int i = 0; i < arrSize; i++) {
        if (arr[i] & 1) {
            count++;
            if (count > 2) {
                return true;
            }
        } else {
            count = 0;
        }
    }

    return false;
}
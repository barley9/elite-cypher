/*
 * 3737. Count Subarrays With Majority Element I
 * 
 * You are given an integer array `nums` and an integer `target`.
 * 
 * Return the number of of `nums` in which `target` is the majority element.
 * 
 * The majority element of a subarray is the element that appears strictly more
 * than half of the times in that subarray.
 */

void print_arr(int* arr, int size) {
    printf("[");
    for (int i = 0; i < size; i++) {
        printf("%i, ", arr[i]);
    }
    printf("]\n");
}

int countMajoritySubarrays(int* nums, int numsSize, int target) {
    /* O(n^2) time, O(n) space solution */
    int count = 0;
    int counts[numsSize + 1];
    counts[0] = count;

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == target) {
            count++;
        }
        counts[i + 1] = count;
    }

    /* print_arr(counts, numsSize + 1); */

    int result = 0;
    for (int stride = 1; stride < 2 * counts[numsSize]; stride++) {
        for (int start = 0; start < numsSize - stride + 1; start++) {
            if ((counts[start + stride] - counts[start]) > (stride / 2)) {
                result++;
            }
        }
    }
    
    return result;
}
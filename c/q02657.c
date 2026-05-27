/*
 * 2657. Find the Prefix Common Array of Two Arrays
 * 
 * You are given two 0-indexed integer permutations `A` and `B` of length `n`.
 * 
 * A prefix common array of `A` and `B` is an array `C` such that `C[i]` is equal
 * to the count of numbers that are present at or before the index `i` in both `A`
 * and `B`.
 * 
 * Return the prefix common array of `A` and `B`.
 * 
 * A sequence of `n` integers is called a permutation if it contains all integers
 * from `1` to `n` exactly once.
 */

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

/*
 * Extremely simple integer hash table implementation
 * NOT included: collision resolution, overfull resolution
 * Based on <https://benhoyt.com/writings/hash-table-in-c/>
 */
typedef struct {
    int* contents;
    int length;
    int capacity;
} hashtable;

#define HT_INITIAL_CAPACITY 256
#define HT_PRIME 1099511628211UL  /* See <https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function#FNV_hash_parameters> */
#define HT_EMPTY_VALUE -1

hashtable* ht_create(void) {
    /* Allocate hashtable struct */
    hashtable* table = malloc(sizeof(hashtable));
    if (table == NULL) {
        printf("Unable to allocate %zu bytes", sizeof(hashtable));
        exit(-1);
    }
    table->capacity = HT_INITIAL_CAPACITY;
    table->length = 0;

    /* Allocate internal contents of hashtable struct */
    table->contents = calloc(table->capacity, sizeof(int));
    if (table->contents == NULL) {
        free(table);  /* free table before exiting! */
        printf("Unable to allocate %zu bytes", table->capacity * sizeof(int));
        exit(-1);
    }

    /* Mark every value as empty */
    for (int i = 0; i < table->capacity; i++) {
        table->contents[i] = HT_EMPTY_VALUE;
    }

    return table;
}

void ht_destroy(hashtable* table) {
    free(table->contents);
    free(table);
}

void ht_insert(hashtable* table, int value) {
    if (table->length + 1 > table->capacity / 2) {
        /* reallocate larger capacity and move values */
    }

    int hash = (value * HT_PRIME) % table->capacity;
    table->contents[hash] = value;  /* ignore possible hash collisions */
    table->length++;
}

void ht_remove(hashtable* table, int value) {
    int hash = (value * HT_PRIME) % table->capacity;
    if (table->contents[hash] == HT_EMPTY_VALUE) {
        /* do something if value doesn't exist in table */
    }
    table->contents[hash] = HT_EMPTY_VALUE;
    table->length--;
}

bool ht_in(hashtable* table, int value) {
    int hash = (value * HT_PRIME) % table->capacity;
    return table->contents[hash] == value;  /* ignore possible collisions */
}

void ht_print(hashtable* table) {
    printf("{");
    for (int i = 0; i < table->capacity; i++) {
        if (table->contents[i] != HT_EMPTY_VALUE) {
            printf("%i, ", table->contents[i]);
        }
    }
    printf("}\n");
}

int* findThePrefixCommonArray(int* A, int ASize, int* B, int BSize, int* returnSize) {
    hashtable* table_a = ht_create();
    hashtable* table_b = ht_create();

    int* result = calloc(ASize, sizeof(int));
    int count = 0;
    for (int i = 0; i < ASize; i++) {
        if (ht_in(table_b, A[i])) {
            count++;
            ht_remove(table_b, A[i]);
        } else {
            ht_insert(table_a, A[i]);
        }

        if (ht_in(table_a, B[i])) {
            count++;
            ht_remove(table_a, B[i]);
        } else {
            ht_insert(table_b, B[i]);
        }

        result[i] = count;
    }

    ht_destroy(table_a);
    ht_destroy(table_b);
    
    *returnSize = ASize;
    return result;
}
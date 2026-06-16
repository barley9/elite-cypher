/*
 * Extremely simple integer hash table implementation
 * NOT included: collision resolution, overfull resolution
 * Based on <https://benhoyt.com/writings/hash-table-in-c/>
 */

#ifndef H_HASHTABLE
#define H_HASHTABLE

#define HT_INITIAL_CAPACITY 256
#define HT_PRIME 1099511628211UL  /* See <https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function#FNV_hash_parameters> */
#define HT_EMPTY_VALUE -1

typedef struct {
    int* contents;
    int length;
    int capacity;
} hashtable;

/* Declarations */
hashtable* ht_create(void);
void ht_destroy(hashtable* table);
void ht_insert(hashtable* table, int value);
void ht_remove(hashtable* table, int value);
bool ht_in(hashtable* table, int value);
void ht_print(hashtable* table);

/* Implementations */
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

#endif
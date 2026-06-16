#define STACK_INITIAL_CAPACITY 16;

typedef struct {
    int capacity;
    int size;
    char* contents;
    char* top;
} Stack;

/* Declarations */
Stack* st_create(void);
void st_expand(Stack* stack);
void st_push(Stack* stack, char c);
char st_pop(Stack* stack);
void st_destroy(Stack* stack);

/* Implementations */
Stack* st_create(void) {
    Stack* stack = malloc(sizeof(Stack));
    if (stack == NULL) {
        printf("Unable to allocate %zu byes", sizeof(Stack));
        exit(-1);
    }
    stack->size = 0;
    stack->capacity = STACK_INITIAL_CAPACITY;
    stack->contents = calloc(stack->capacity, sizeof(char));
    if (stack->contents == NULL) {
        free(stack);
        printf("Unable to allocate %zu byes", stack->capacity * sizeof(char));
        exit(-1);
    }
    stack->top = stack->contents;

    return stack;
}

void st_expand(Stack* stack) {
    /* Double the capacity */
    char* new_contents = calloc(2 * stack->capacity, sizeof(char));
    if (new_contents == NULL) {
        st_destroy(stack);
        printf("Unable to allocate %zu byes", 2 * stack->capacity * sizeof(char));
        exit(-1);
    }
    
    /* Copy over contents */
    for (int i = 0; i < stack->size; i++) {
        new_contents[i] = stack->contents[i];
    }

    /* Reassign pointers */
    stack->top = new_contents + stack->size;
    stack->contents = new_contents;
}

void st_push(Stack* stack, char c) {
    if (stack->size >= stack->capacity) {
        st_expand(stack);
    }
    *stack->top = c;
    stack->top++;
    stack->size++;
}

char st_pop(Stack* stack) {
    if (stack->size <= 0) {
        printf("attempted to pop() from empty stack");
        exit(-1);
    }

    stack->top--;
    stack->size--;
    return *stack->top;
}

void st_destroy(Stack* stack) {
    free(stack->contents);  /* don't free() `stack->top`! */
    free(stack);
}

void st_print(Stack* stack) {
    
}


char* processStr(char* s) {
    Stack* result = st_create();
    
    char* c = s;
    while (*c) {
        switch (*c) {
            case '*':
                if (result->size > 0) st_pop(result);
                break;
            case '#':
                break;
            case '%':
                break;
            default:
                st_push(result, *c);
        }
        c++;
    }

    return result->contents;
}

/* ********** */

char* processStr(char* s) {
    int capacity = 256;
    int size = 0;
    char result[capacity];
    for (int i = 0; i < capacity; i++) {
        result[i] = 0;
    }
    char* top = result;

    char* c = s;
    while (*c) {
        switch (*c) {
            case '*':
                if (size > 0) {
                    top--;
                    *top = 0;
                    size--;
                }
                break;
            case '#':
                capacity = 2 * capacity;
                char new_result[capacity];
                strcpy(new_result, result);
                strcpy(new_result + size, result);
                top = new_result + 2 * size;
                result = new_result;
                break;
            case '%':
                char new_result[capacity] = 0;
                for (int i = 0; i < size; i++) {
                    *(new_result + i) = *(top - i);
                }
                result = new_result;
                break;
            default:
                if (size >= capacity) {
                    capacity = 2 * capacity;
                    char new_result[capacity];
                    for (int i = 0; i < capacity; i++) {
                        new_result[i] = 0;
                    }
                    strcpy(new_result, result);
                    top = new_result + size;
                    result = new_result;
                }
                *top = *c;
                top++;
                size++;
        }
    }

    return result;
}
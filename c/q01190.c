/*
 * 1190. Reverse Substrings Between Each Pair of Parentheses
 * 
 * You are given a string `s` that consists of lower case English letters and
 * brackets.
 * 
 * Reverse the strings in each pair of matching parentheses, starting from the
 * innermost one.
 * 
 * Your result should not contain any brackets.
 */


#define STACK_INITIAL_CAPACITY 2048

typedef struct {
    char* data;
    char* top;
} Stack;

Stack* sk_create(void) {
    Stack* stack = malloc(sizeof(Stack));
    stack->data = calloc(STACK_INITIAL_CAPACITY, sizeof(char));
    stack->top = stack->data;  /* first empty address on stack */

    return stack;
}

void sk_clear(Stack* stack) {
    stack->top = stack->data;
}

int sk_size(Stack* stack) {
    return stack->top - stack->data;
}

void sk_push(Stack* stack, char val) {
    *stack->top = val;
    stack->top++;
}

char sk_pop(Stack* stack) {
    if (stack->top <= stack->data) {
        printf("attempted pop() from empty stack");
        exit(-1);
    }
    return *(--stack->top);
}

char sk_peek(Stack* stack) {
    return *(stack->top - 1);
}

void sk_destroy(Stack* stack) {
    free(stack->data);  /* don't free `top` because it points into `data` */
    free(stack);
}

char* reverseParentheses(char* s) {
    /* O(n) time, O(n) space solution */
    Stack* stack = sk_create();
    Stack* temp  = sk_create();

    char* c = s;
    while (*c != '\0') {
        printf("c = %c\n", *c);
        if (*c == ')') {
            sk_clear(temp);
            while (sk_peek(stack) != '(') {
                sk_push(temp, sk_pop(stack));
            }
            sk_pop(stack);  /* pop '(' from `stack` */

            /* Append `temp` contents to `stack` */
            char* p = temp->data;
            while (p < temp->top) {
                sk_push(stack, *p);
                p++;
            }
        } else {
            *stack->top = *c;
            stack->top++;
        }
        c++;
    }
    sk_destroy(temp);  /* don't destroy `stack` because we return its internals */

    *stack->top = '\0';  /* add null-terminator */
    return stack->data;
}
/*
 * Extremely simple char stack implementation
 * NOT included: overfull resolution
 */

#ifndef STACK_HEADER_H
#define STACK_HEADER_H

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
        printf("attempted pop() from empty stack\n");
        exit(-1);
    }
    return *(--stack->top);
}

char sk_peek(Stack* stack) {
    return *(stack->top - 1);
}

void sk_print(Stack* stack) {
    *stack->top = '\0';
    printf("[%s]\n", stack->data);
}

void sk_destroy(Stack* stack) {
    free(stack->data);  /* don't free `top` because it points into `data` */
    free(stack);
}

#endif  /* STACK_HEADER_H */
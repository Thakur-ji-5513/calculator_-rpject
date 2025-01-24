#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int add(int a, int b);
int sub(int a, int b);
int mult(int a, int b);
int my_div(int a, int b);
int power(int a, int b);

int main(int argc, char *argv[]) {
    if (argc != 4) {
        printf("Usage: %s <num1> <num2> <operation>\n", argv[0]);
        return 1;
    }

    int a = atoi(argv[1]);
    int b = atoi(argv[2]);
    char operation = argv[3][0]; // Get the first character of the operator string
    int result;

    switch (operation) {
        case '+':
            result = add(a, b);
            break;
        case '-':
            result = sub(a, b);
            break;
        case '*':
            result = mult(a, b);
            break;
        case '/':
            if (b == 0) {
                printf("Error: Division by zero is not possible\n");
                return 1;
            }
            result = my_div(a, b);
            break;
        case '^':
            result = power(a, b);
            break;
        default:
            printf("Invalid operation\n");
            return 1;
    }

    printf("%d\n", result);
    return 0;
}

int add(int a, int b) {
    return a + b;
}

int sub(int a, int b) {
    return a - b;
}

int mult(int a, int b) {
    return a * b;
}

int my_div(int a, int b) {
    return a / b;
}

int power(int a, int b) {
    return (int)pow(a, b);  // Cast the result of pow to int
}

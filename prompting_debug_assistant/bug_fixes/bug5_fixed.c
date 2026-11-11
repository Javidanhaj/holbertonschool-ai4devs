/* Goal: Sum every element of an integer array. */
#include <stdio.h>
#include <stddef.h>

int sum_array(const int numbers[], size_t count)
{
    int total = 0;

    for (size_t i = 0; i < count; i++) {
        total += numbers[i];
    }
    return total;
}

int main(void)
{
    int values[] = {1, 2, 3, 4, 5};
    printf("Sum: %d\n", sum_array(values, sizeof(values) / sizeof(values[0])));
    printf("Expected sum: 15\n");
    return 0;
}

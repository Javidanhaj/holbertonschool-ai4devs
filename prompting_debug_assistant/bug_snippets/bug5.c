/* Goal: Sum every element of an integer array. */
#include <stdio.h>

int sum_array(int numbers[])
{
    int count = sizeof(numbers) / sizeof(numbers[0]);
    int total = 0;

    for (int i = 0; i < count; i++) {
        total += numbers[i];
    }
    return total;
}

int main(void)
{
    int values[] = {1, 2, 3, 4, 5};
    printf("Sum: %d\n", sum_array(values));
    printf("Expected sum: 15\n");
    return 0;
}

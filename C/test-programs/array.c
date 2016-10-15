#include <stdlib.h>
#include <stdio.h>
int main(){
        /* How do you define the beginning block comment */
        int *array = malloc(100*sizeof(array));
        int sum = 0;
        int i;
        for (i = 0; i < 100; ++i) {
                array[i] = i*i;
                sum += array[i];
        }
        printf("sum: %d\n", sum);
        return 0;
        
}

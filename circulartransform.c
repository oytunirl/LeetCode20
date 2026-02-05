#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int* constructTransformedArray(int* nums, int numsSize, int* returnSize) {
    int * res = (int *)malloc(sizeof(int) * numsSize);
    int temp = 0;

    for (size_t i = 0; i < numsSize; i++)
    {
        temp = nums[i];
        if(temp > 0){
            int index = (i + (nums[i] % numsSize)) % numsSize;
            res[i] = nums[index];
        }else if(temp < 0){
            int shift = nums[i] % numsSize;
            int index = (i + shift + numsSize) % numsSize;
            res[i] = nums[index];
        }else{
            res[i] = nums[i];
        }
    }

    *returnSize = numsSize;

    return res;
}

int main() {
    int nums[] = {3, -2, 1, 1};
    int returnSize;
    int* result = constructTransformedArray(nums, 4, &returnSize);
    printf("Transformed Array: ");
    for (int i = 0; i < returnSize; i++) {
        printf("%d ", result[i]);
    }
    printf("\n");
    free(result);
    return 0;
}
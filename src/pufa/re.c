#include "pufa.h"

int pfre( int * nums, int numsSize ){
    int s = (numsSize + 1) / 2 - 1;
    int tmp;

    for( int i = 0; i <= s; i++ ){
        tmp = nums[i];
        nums[i] = nums[numsSize-i-1];
        nums[numsSize-i-1] = tmp;
    }

    return 0;
}

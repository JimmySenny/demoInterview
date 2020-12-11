#include "pufa.h"


void tst_pfre( void ){
    int nums1[4] = {1,2,3,4};
    int nums2[7] = {1,2,3,4,5,6,7};

    printNums( nums1, 4 );
    printNums( nums2, 7 );

    pfre( nums1, 4 );
    pfre( nums2, 7 );

    printNums( nums1, 4 );
    printNums( nums2, 7 );

    return;
}

void tst_pfsum( void ){
    double sum = 0;

    pfsum( 1, &sum );
    printf( "sum=[%lf]\n", sum );

    pfsum( 2, &sum );
    printf( "sum=[%lf]\n", sum );

    pfsum( 3, &sum );
    printf( "sum=[%lf]\n", sum );
}

void tst_addBinary(){
    char s1[] = "1111";
    char s2[] = "1111";

    printf( "addBinary[%s]", addBinary(s1,s2));

    return;
}


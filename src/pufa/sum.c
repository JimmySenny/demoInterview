#include "pufa.h"

int pfsum( int _num, double *_sum ){
    double n;
    
    if( _num <= 0 ){
        return -1;
    }

    *_sum = 0;
    for( int i = 1; i <= _num; i++ ){
        n = (double)i/(2*i-1);
        *_sum += n;
    }

    return 0;
}

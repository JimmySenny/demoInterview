#include "pufa.h"

char * addBinary(char *a, char *b){
    int lena = strlen(a);
    int lenb = strlen(b);
    int lenmax = (lena>lenb)?lena:lenb;
    int carry = 0;
    int i = 0, j = 0;
    int n1 = 0, n2 = 0, n = 0;
    char *ans = malloc(sizeof(char) * (lenmax + 2)); //末尾及可能的进位
    memset( ans, 0x00, sizeof(char) * (lenmax + 2));
    ans[0] = '0';
    for( int k = 0; k < lenmax;k++,i++,j++){
        n1 = (i<lena)?(a[lena-i-1]-'0'):0;
        n2 = (j<lenb)?(b[lenb-i-1]-'0'):0;
        n = n1 + n2 + carry;
        carry = (n > 1)?1:0;
        ans[k] = '0' + n%2;
    }
    if(carry){
        strcat(ans,"1");
    }

    printf("ansre[%s]\n", ans);

    lenmax = strlen(ans);
    char ch;
    for( i = 0; i < (lenmax + 1)/2; i++){
        ch = ans[i];
        ans[i] = ans[lenmax -1-i];
        ans[lenmax -1 -i] = ch;
    }

    return ans;
}

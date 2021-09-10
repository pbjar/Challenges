#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define mxn 1000100
#define max(x, y) ((x) > (y) ? (x) : (y))
#define swap(x, y) ((x) ^= (y), (y) ^= (x), (x) ^= (y))

/* READLINE TEMPLATE */

int readline(char *s){
    char *t = s;
    while((*t = getchar()) != '\n') t++;
    int ret = strlen(s) - 1;
    *t = '\0';
    return ret;
}

/* END READLINE TEMPLATE */

/* KMP TEMPLATE */

int m;
int a[mxn << 1];
char b[mxn << 1];

int kmp(){
        for(int i = 1; i < m; i++){
                a[i] = a[i - 1];
                while(a[i] && b[i] != b[a[i]]) a[i] = a[a[i] - 1];
                a[i] += b[i] == b[a[i]];
        }
        return a[m - 1];
}

/* END KMP TEMPLATE */

void answer(){
        char s[mxn];
        
        int n = readline(s); 

        //find characters equal along prefix and suffix, always optimal to choose these
        int k = 0;
        while(2 * k + 1 < n && s[k] == s[n - k - 1]) k++;

        m = 2 * (n - 2 * k) + 1;

        //find largest palindrome that is prefix or suffix of the middle string with kmp
        int f[2];
        for(int i = 0; i < 2; i++){
                //create string (s + # + s'), where s' is reverse of s
                memcpy(b, s + k, m / 2);
                b[m / 2] = '#';
                //reverse the string to try other side
                for(int j = k; 2 * j + 1 < n; j++) swap(s[j], s[n - j - 1]);
                memcpy(b + m / 2 + 1, s + k, m / 2);
                f[i] = kmp();
        }

        //get larger sol
        if(f[1] > f[0]) memcpy(s + k, s + n - k - f[1], f[1]);
        memcpy(s + k + max(f[0], f[1]), s + n - k, k);
        s[2 * k + max(f[0], f[1])] = '\0';
        
        puts(s);
        
	//reset string
        s[2 * k + max(f[0], f[1])] = '#';
        for(m = 0; s[m]; m++) s[m] = '\0';
}

int main(){
        setbuf(stdout, 0x0);
        setbuf(stderr, 0x0);

        int t = 1;
        scanf("%d\n", &t); //uncomment to read multiple testcases

        for(int i = 0; i < t; i++) answer();

        return 0;
}

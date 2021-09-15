#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define mxn 201
#define max(x, y) ((x) >= (y) ? (x) : (y))

int n, k;
char s[mxn], t[3];
int dp[mxn][mxn], dq[mxn][mxn];

int main(){
	setbuf(stdout, 0x0);
        setbuf(stderr, 0x0);
	
	memset(dp, 0xcf, sizeof(dp));
	dp[0][0] = 0;

	scanf("%d%d", &n, &k);
	getchar();

	assert(n >= 2 && n < mxn && k >= 0 && k <= n);

	fgets(s, n + 1, stdin);
	getchar();
	gets(t);

	//dynamic programming to hold best solution at different states, adding one char of s at a time
	//dp[j][l] = best sol with j substitutions, and l chars equal to t[0]
	for(int i = 0; i < n; i++){
		memcpy(dq, dp, sizeof(dp));
		memset(dp, 0xcf, sizeof(dp));
		for(int j = 0; j <= k; j++)
		for(int l = 0; l <= n; l++){
			int x = s[i] == t[0];
			if(l >= x) dp[j][l] = max(dp[j][l], dq[j][l - x] + (l - x) * (s[i] == t[1]));
			if(j && l) dp[j][l] = max(dp[j][l], dq[j - 1][l - 1] + (l - 1) * (t[0] == t[1]));
			if(j) dp[j][l] = max(dp[j][l], dq[j - 1][l] + l);
		}
	}

	int ret = -1;
	for(int i = 0; i <= n; i++) ret = max(ret, dp[k][i]);

	if(!~ret){
		puts("Uh oh, this isn't supposed to happen.");

		FILE *f = fopen("flag.txt", "r");
		if(f == NULL){
			puts("If you are running locally, you need to place flag.txt in the running directory.");
			puts("Otherwise, a problem has occured. Please contact the author on discord.");
			exit(1);
		}

		char flag[0x40];
		fgets(flag, 0x40, f);

		puts("DEBUG:");
		puts(flag);
	}

	printf("%d\n", ret);

	return 0;	
}

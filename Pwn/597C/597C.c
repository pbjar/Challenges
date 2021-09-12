#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define ll long long

/*BIT TEMPLATE*/

#define k 17

void add(ll b[1 << k], int x, ll y){
	for(x++; x > 0 && x < (1 << k); x += x & -x) b[x] += y;
}

ll qry(ll b[1 << k], int x){
	ll ret = 0;
	for(x++; x > 0 && x < (1 << k); x -= x & -x) ret += b[x];
	return ret;
}

int lbd(ll b[1 << k], ll x){
	int ret = 0;
	for(int i = k - 1; ~i; i--){
		int y = ret | (1 << i);
		if(x > b[y]) x -= b[ret = y];
	}
	return ret;
}

/*END BIT TEMPLATE*/

#define mxn 122222
#define mxm 12

int n, m;
int a[mxn];

void answer(){
	scanf("%d%d", &n, &m);
	m++;

	assert(n >= 1 && n < mxn && m >= 1 && m < mxm);

	for(int i = 0; i < n; i++){
	       	scanf("%d", &a[i]);
		assert(a[i] >= 1 && a[i] <= n);
	}

	ll b[mxm][mxn];
	memset(b, 0, sizeof(b));

	//add elements one by one and hold number of increasing subsequences ending at each value
	//use BIT to quickly transition by counting subsequences of length j - 1 that could append a[i]
	add(b[0], 0, 1);
	for(int i = 0; i < n; i++)
	for(int j = 1; j <= m; j++){
		add(b[j], a[i], qry(b[j - 1], a[i] - 1)); 
	}

	printf("%lld\n", qry(b[m], n));
}

int main(){
	setbuf(stdout, 0x0);
        setbuf(stderr, 0x0);

	int t = 1;
	//scanf("%d", &t); //uncomment for problems with multiple testcases

	for(int i = 0; i < t; i++) answer();

	return 0;	
}

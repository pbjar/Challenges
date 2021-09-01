#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define stonk_num 0x30

char user_buf[0x130];

char* pick_symbol_with_AI(){
        char *ret = calloc(0x5, 0x1);

        for(int i = 0; i < 4; i++){
                char x = rand();
                ret[i] = x + (x / 0x1a) * -0x1a + 'A';
        }

        ret[4] = '\0';

        return ret;
}

void init_stonks(char *stonk[stonk_num]){
	puts("\nBuying stonks...");
		
	for(int i = 0; i < stonk_num; i++) stonk[i] = pick_symbol_with_AI();
}

void buy_stonks(char *stonk[stonk_num]){
	puts("What stonk do you want to see?");

	int x;
	scanf("%d", &x);

	if(x < 0 || x >= stonk_num){
		puts("You think we haven't fixed this STILL!");
		puts("Invalid index.");
		exit(0);
	}

	stonk = (char **)((int)stonk + 4 * x);

	puts(*stonk);

	puts("\nWhat is your API token?");
	getchar();
	user_buf[read(0x0, user_buf, 0x12c)] = '\0';
	puts("");

	for(int i = 0; i < 0x12c; i++){
		switch(user_buf[i]){
                       	case 0x41:
                       	case 0x45:
                       	case 0x46:
                       	case 0x47:
                       	case 0x58:
                       	case 0x61:
                       	case 0x64:
                       	case 0x65:
                       	case 0x66:
                       	case 0x67:
                       	case 0x69:
                       	case 0x6f:
                       	case 0x70:
                       	case 0x73:
                       	case 0x75:
                       	case 0x78:
				puts("Hey! Only one leak allowed!");
                               	exit(1);
		}
	}

	puts("Buying stonks with token:");
	printf(user_buf);
}

int main(){
        setbuf(stdout, 0x0);
        setbuf(stderr, 0x0);
        srand(time(0));

	puts("You are at a familiar seeming place, somewhere between 32nd and wall street.");
        puts("Welcome back to the trading app!\n");

        puts("What would you like to do?");
        puts("1) Buy some stonks!");

        int choice;
        scanf("%d", &choice);

        if(choice == 1){
		char *stonk[stonk_num];
		init_stonks(stonk);
		buy_stonks(stonk);
	}

        return 0;
}

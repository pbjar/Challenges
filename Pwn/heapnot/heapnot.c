#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define n 32

int siz[n];
char *not[n];

char* mallocx(long sz){
	puts("This cod section is incomplet. W will work on finishing it soon.");
	_exit(1);
}

void menu(char *buf){
	puts("Your options are:");
	puts("1) creat");
	puts("2) delet");
	puts("3) edit");
	puts("4) display");
	puts("5) exit\n");
	
	puts("What would you lik to do?");
	buf[read(0x0, buf, 0x4000) - 1] = '\0';
	puts("");
}

void invalid(char *mes){
	printf("Invalid %s.\n", mes);
	_exit(1);
}

int inidx(){
        int idx;
        scanf("%d", &idx);
	getchar();
	puts("");
        if(idx < 0 || idx >= n) invalid("index, out of bounds");
	return idx;
}

void creat(){
	puts("You get to creat a not.\n");

	puts("Which index would you lik to creat a not at?");
	int idx = inidx();

	if(not[idx]) invalid("index, already exists");

	puts("What siz would you lik your not to b?");
	scanf("%d", &siz[idx]);
	getchar();
	puts("");

	if(siz[idx] <= 0 || siz[idx] > 0x1000) invalid("siz, out of bounds");

	not[idx] = mallocx(siz[idx] + 1);

	puts("Not created.\n");
}

void delet(){
	puts("You get to delet a not.\n");

	puts("Which index would you lik to delet a not from?");
	int idx = inidx();

	if(!not[idx]) invalid("index, does not exist");

	free(not[idx]);
	not[idx] = 0;

	puts("Not deleted.\n");
}

void edit(){
	puts("You get to edit a not.\n");

	puts("Which index would you lik to edit a not at?");
	int idx = inidx();

	if(!not[idx]) invalid("index, doest not exist");

	puts("What messag would you lik th not to contain?");
	not[idx][read(0x0, not[idx], siz[idx] + 1) - 1] = '\0';
	puts("");

	puts("Not edited.\n");
}
	
void display(){
	puts("You get to display a not.\n");

	puts("Which index would you lik to display a not from?");
	int idx = inidx();

	if(!not[idx]) invalid("index, does not exist");

	printf("This not contains the messag: %s\n\n", not[idx]);

	puts("Not displayed.\n");
}

void stkspace(){
        puts("Welcom to my first heapnot challeng.");
	printf("Her is a gift sinc it is th first challeng: %p\n\n", (long)free & 0xffffff);
	
	for(int x = 0; x != 5;){
		char buf[0x20];
		menu(buf);
		x = atoi(buf);
		switch(x){
			case 1:
				creat();
				break;
			case 2:
				delet();
				break;
			case 3:
				edit();
				break;
			case 4:
				display();
				break;
			case 5:
				puts("Bye.");
				break;
			default:
				invalid("option, does not exist");
				break;
		}
	}

	close(0x1);
}

int main(){
	char stk[0x4000];

	stkspace();

	_exit(0);

	return 0;
}

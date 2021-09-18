#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define n 32

char secret_messag[] = "Good luck on this problem! I think it is pretty geniosity, hopefully you do too.";
char secret_messag2[] = "I wonder why i'm putting these random strings here anyway. Perhaps it's for a reason?";
int siz[n];
char *not[n];

void freex(char *ptr){
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
	
	puts("What would you lik to do (enter option in format \"[number] go!\")?");
	for(int i = 0; i < 0x4000; i++){
		buf[i] = getchar();
		buf[i + 1] = '\0';
		if(i >= 4 && !strcmp(" go!\n", buf + i - 4)){
			buf[i - 4] = '\0';
			break;
		}
	}
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

	not[idx] = malloc(siz[idx] + 1);

	puts("Not created.\n");
}

void delet(){
	puts("You get to delet a not.\n");

	puts("Which index would you lik to delet a not from?");
	int idx = inidx();

	if(!not[idx]) invalid("index, does not exist");

	freex(not[idx]);
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
        puts("Welcom to my heapnot challeng.");
	puts("I got a bit carried away...\n");

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

	close(0x0);
	close(0x1);
	close(0x2);
}

int main(){	
	char stk[0x4000];

	stkspace();

	_exit(0);

	return 0;
}

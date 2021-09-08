#include <stdio.h>
#include <stdlib.h>

int main(){
	setbuf(stdout, 0x0);
        setbuf(stderr, 0x0);

	char stkbuf[0x80];
	char *heapbuf = malloc(0x80);

	puts("Oh no! Evil Morty is attempting to open the central finite curve!");
	puts("You get three inputs to try to stop him.\n");

	puts("Input 1:");
        read(0x0, stkbuf, 0xb0);
        printf("%s\n", stkbuf);

        puts("Input 2:");
        read(0x0, stkbuf, 0x80);

        puts("\nInput 3:");
        read(0x0, heapbuf, 0x80);
        printf(heapbuf);

        free(heapbuf);

	puts("\nLol how could inputting strings stop the central finite curve.");

	_exit(0);

	return 0;	
}

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define n 8

int isopen[n], isread[n], size[n];
FILE *song[n];
char *lyrics[n];

int menu(){
	puts("Your options are:");
	puts("1) open song");
	puts("2) close song");
	puts("3) read lyrics");
	puts("4) display lyrics");
	puts("5) shutdown bot\n");
	
	int ret;
	puts("What would you like to do?");
	scanf("%d", &ret);
	getchar();
	puts("");

	return ret;
}

void invalid(char *mes){
	printf("Invalid - %s.\n", mes);
	_exit(1);
}

int inidx(){
        int idx;
        scanf("%d", &idx);
	getchar();
	puts("");
        if(idx < 0 || idx >= n) invalid("index out of bounds");
	return idx;
}

void open_song(){
	puts("You get to open a song.\n");

	puts("What index would you like to store the song at?");
	int idx = inidx();

	if(isopen[idx]) invalid("index already contains open song");

	puts("What song would you like to open?");
	char buf[0x80] = "/songs/";
	scanf("%120s", buf + 7);
	puts("");

	song[idx] = fopen(buf, "r");
	isopen[idx] = 1;
	if(isread[idx]) free(lyrics[idx]);
	isread[idx] = 0;

	if(!song[idx]) invalid("song does not exit");

	puts("Song opened.\n");
}

void close_song(){
	puts("You get to close a song.\n");

	puts("Which index would you like to close a song from?");
	int idx = inidx();

	if(!isopen[idx]) invalid("index does not contain open song");

	fclose(song[idx]);
	isopen[idx] = 0;

	puts("Song closed.\n");
}

void read_lyrics(){
	puts("You get to read lyrics of a song.\n");

	puts("Which index would you like to read lyrics of a song from?");
	int idx = inidx();

	if(isread[idx]) invalid("lyrics already read for this song");
	
	puts("How much of the lyrics would you like to read?");
	scanf("%d", &size[idx]);
	getchar();
	puts("");

	if(size[idx] <= 0 || size[idx] >= 0x1000) invalid("size out of range");

	lyrics[idx] = malloc(size[idx] + 1);
	lyrics[idx][fread(lyrics[idx], 1, size[idx], song[idx])] = '\0';
	isread[idx] = 1;

	puts("Lyrics read.\n");
}
	
void display_lyrics(){
	puts("You get to display lyrics of a song.\n");

	puts("Which index would you like to display lyrics of a song from?");
	int idx = inidx();

	if(!isread[idx]) invalid("lyrics not yet read for this song");

	puts("The lyrics for this song is:");
	puts(lyrics[idx]);
	puts("");

	puts("Lyrics displayed.\n");
}

void shutdown_bot(){
	puts("You're not gonna sing for him?!");
	for(int i = 0; i < n; i++){
		if(isread[i]) free(lyrics[i]), fclose(song[i]);
		else if(isopen[i]) fclose(song[i]);
	}
	_exit(0);
}

int main(){
	setbuf(stdout, 0);
	setbuf(stderr, 0);

	puts("\"My brother came all the way out here from Scottsdale, Arizona, and you’re not gonna sing for him?!\"\n");

        puts("Are you being asked to sing randomly for people's brothers, but don't know any song lyrics?");
	puts("Well luckily, I've got the thing for you!\n");

	puts("I made a new service called \"RothmBot\" which can show you lyrics to a vareity of songs :yayy:!");
	puts("They lyrics are in song1.txt, song2.txt, etc.\n");

	puts("Hopefully you can now sing for anyone's brother who came from Scottsdale Arizona!\n");

	while(1){
		int x = menu();
		switch(x){
			case 1:
				open_song();
				break;
			case 2:
				close_song();
				break;
			case 3:
				read_lyrics();
				break;
			case 4:
				display_lyrics();
				break;
			case 5:
				shutdown_bot();
				break;
			default:
				invalid("option does not exist");
				break;
		}
	}

	return 0;
}

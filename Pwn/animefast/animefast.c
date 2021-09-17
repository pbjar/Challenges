#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define n 16
#define m 56
#define tsz 100
#define dsz 176
#define csz 32

int numanimes;
struct show{
	char *title;
	char description[dsz];
	int numcharacters;
	char *character[m]
} *anime[n];

void invalid(char *mes){
	printf("Invalid - %s.\n", mes);
	_exit(1);
}

int addanime(char *buf, char *buf2){
	int idx = numanimes++;
	if(idx == n) invalid("no more anime slots available");
	anime[idx] = malloc(sizeof(struct show));
	anime[idx]->title = malloc(tsz);
	strcpy(anime[idx]->title, buf);
	strcpy(anime[idx]->description, buf2);
	anime[idx]->numcharacters = 0;
	return idx;
}

int addcharacter(int idx, char *buf){
	if(idx < 0 || idx >= numanimes) invalid("anime index out of range");
	int idy = anime[idx]->numcharacters++;
	if(idy == m) invalid("no more characters slots available for this anime");
	anime[idx]->character[idy] = malloc(csz);
	strcpy(anime[idx]->character[idy], buf);
	return idy;
}

void removecharacter(int idx, int idy){
	if(idx < 0 || idx >= numanimes) invalid("anime index out of range");
	if(idy < 0) invalid("character index out of range");
	if(!anime[idx]->character[idy]) invalid("character does not exist at given index");
	int idz = --anime[idx]->numcharacters;
	if(idz < 0) invalid("no characters currently added for this anime");
	free(anime[idx]->character[idy]);
	anime[idx]->character[idy] = anime[idx]->character[idz];
	anime[idx]->character[idz] = 0;
}

void init_anime(){
	addanime("Saenai Heroine no Sodatekata - Saekano", "A romantic comedy where high school student Tomoya Aki recruits a trio of beautiful girls to help him develop a visual novel to sell at the Comiket convention.");
	addcharacter(0, "Tomoya Aki");
	addcharacter(0, "Megumi Kato");
	addcharacter(0, "Eriri Spencer Sawamura");
	addcharacter(0, "Utaha Kasumigaoka");
	addcharacter(0, "Michiru Hyodo");
	addcharacter(0, "Izumi Hashima");
	addcharacter(0, "Michiru Hyodo");
	addcharacter(0, "Iori Hashima");
	addcharacter(0, "Akane Kosaka");
	addcharacter(0, "Sonoko Machida");
	addcharacter(0, "Tokino Himekawa");
	addcharacter(0, "Echika Mizuhara");
	addcharacter(0, "Ranko Morioka");
}

int inidx(){
        int idx;
        scanf("%d", &idx);
	getchar();
	puts("");
	return idx;
}

void inbuf(char *buf, int sz){
	buf[read(0x0, buf, sz) - 1] = '\0';
	puts("");
}

int menu(){
	puts("Your options are:");
	puts("1) add anime");
	puts("2) add character");
	puts("3) remove character");
	puts("4) display animes");
	puts("5) exit\n");
	
	puts("What would you like to do?");

	return inidx();
}

void add_anime(){
	puts("You get to add an anime.\n");


	puts("What is the anime's title?");
	char buf[tsz];
	inbuf(buf, tsz);

	puts("What is the description of the anime?");
	char buf2[dsz];
	inbuf(buf2, dsz);

	int idx = addanime(buf, buf2);	

	printf("Anime #%d added.\n\n", idx);
}

void add_character(){
	puts("You get to add a character to an anime.\n");

	puts("Which index of anime would you like to add the character to?");
	int idx = inidx();

	if(!idx) invalid("cannot edit anime #0");

	puts("What is the character's name?");
	char buf[csz];
	inbuf(buf, csz);

	int idy = addcharacter(idx, buf);

	printf("Character #%d added to anime #%d.\n\n", idy, idx);
}

void remove_character(){
	puts("You get to remove a character from an anime.\n");

	puts("Which index of anime would you like to remove the character from?");
	int idx = inidx();

	if(!idx) invalid("cannot edit anime #0");

	puts("What index of chracter from the anime would you like to remove?");
	int idy = inidx();

	removecharacter(idx, idy);

	printf("Character #%d removed from anime #%d.\n\n", idy, idx);
}

void displaydiv(){
	puts("-------------------------------------------------");
}

	
void display_animes(){
	puts("The animes currently added will now be displayed.\n");

	for(int idx = 0; idx < numanimes; idx++){
		displaydiv();
		printf("Anime #%d: %s\n", idx, anime[idx]->title);
		displaydiv();
		printf("Description: %s\n", anime[idx]->description);
		displaydiv();
		if(anime[idx]->numcharacters){
			for(int idy = 0; idy < anime[idx]->numcharacters; idy++){
				printf("Character #%d: %s\n", idy, anime[idx]->character[idy]);
			}
		}else{
			puts("Currently no characters added to this anime.");
		}
		displaydiv();
		puts("");
	}

	puts("Animes displayed.\n");	
}

int main(){
	setbuf(stdin, 0);
	setbuf(stdout, 0);
	setbuf(stderr, 0);

        puts("Hello weeb!\n");

	puts("I created a new service called \"AnimeFast\" to quickly record your favorite animes and characters.");
	puts("Now you can keep track of all the best shows and compare with your friends :yayy:!\n");

	init_anime();

	puts("Also, I added one of my own favorite anime as an example.");
	puts("You can see it as anime #0 if you display animes.\n");

	puts("I hope you find AnimeFast helpful!\n");

	while(1){
		int x = menu();
		switch(x){
			case 1:
				add_anime();
				break;
			case 2:
				add_character();
				break;
			case 3:
				remove_character();
				break;
			case 4:
				display_animes();
				break;
			case 5:
				puts("Bye.");
				_exit(0);
				break;
			default:
				invalid("option does not exist");
				break;
		}
	}
}

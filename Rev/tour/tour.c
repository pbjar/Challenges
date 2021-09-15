#include <stdio.h>
#include <stdlib.h>

int cost[15][15] = {
{753, 8162, 966, 8341, 980, 1500, 77, 966, 7308, 372, 4326, 9038, 726, 9430, 333}
, {410, 2574, 2437, 6532, 788, 242, 9622, 102, 911, 905, 875, 328, 953, 5501, 5941}
, {9095, 85, 511, 434, 4958, 2190, 482, 945, 114, 912, 922, 4044, 616, 70, 539}
, {839, 180, 198, 995, 7151, 1941, 650, 3351, 154, 292, 403, 279, 270, 4953, 108}
, {6932, 658, 474, 350, 7883, 779, 643, 5473, 6742, 363, 309, 825, 780, 2015, 446}
, {3513, 7711, 3491, 621, 7294, 15, 6563, 4190, 5487, 8027, 126, 623, 7846, 306, 155}
, {9896, 830, 569, 391, 3449, 1170, 5082, 7035, 682, 832, 3273, 47, 9587, 720, 4603}
, {651, 4317, 235, 914, 3989, 8365, 6015, 6035, 85, 629, 842, 4055, 3272, 3484, 9495}
, {8468, 62, 680, 5938, 443, 368, 4370, 916, 866, 9227, 8164, 868, 4948, 6888, 7863}
, {483, 5412, 894, 2128, 898, 8788, 976, 171, 466, 5868, 392, 154, 7256, 391, 5326}
, {9504, 324, 965, 62, 9627, 5319, 4618, 803, 431, 7679, 339, 529, 517, 5923, 525}
, {6056, 7461, 1692, 249, 787, 5258, 782, 3129, 958, 6490, 3927, 3068, 479, 4553, 103}
, {9302, 251, 9511, 5496, 120, 6370, 866, 8780, 799, 3699, 175, 4916, 6503, 1695, 3114}
, {21, 5639, 7543, 6146, 9792, 1016, 7657, 8461, 163, 136, 2183, 337, 4453, 131, 8538}
, {1387, 296, 619, 6983, 4606, 594, 18, 107, 4985, 6694, 797, 4299, 521, 2093, 701}
};

int vis = (1<<15)-1;

int main(){
    setlinebuf(stdout);
    printf("hi can you plan me a tour around the world that doesn't make me broke thanks\n");
    printf("if the tour makes me happy then i'll give you the flag :)\n");
    int money = 2200;
    int city = 0;
    while(money >= 0){
        printf("\n");
        if(!vis && city == 0){
            printf("i like this tour\n");
            printf("i guess i'll give you the flag now\n");
            FILE *f = fopen("flag.txt", "rb");
            if(!f){
                printf("If this is running on the server, please contact an admin.\n");
                return 0;
            }
            char *flag = malloc(40);
            fread(flag, 1, 39, f);
            printf("%s", flag);
            return 0;
        }
        printf("im not happy with the tour yet\n");
        printf("where to go next???\n");
        int nxt;
        scanf("%d", &nxt);
        if(nxt < 0 || nxt >= 15){
            printf("i don't like that city\n");
        }else{
            money -= cost[city][nxt];
            city = nxt;
            vis &= ~(1<<city);
        }
        int c;
        while ((c = getchar()) != '\n' && c != EOF) { }
    }
    printf("aw man im broke now\n");
    printf("no flag for you\n");
}

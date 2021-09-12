#include <stdio.h>
#include <curl/curl.h>

int main(void){
    CURL *curl;
    CURLcode res;
    FILE *fp;
    char *nversion = "v2";
    char *url = "http://137.184.108.185/v2";
    curl = curl_easy_init();
    printf("Updating to version %s...\n", nversion);
    if(curl){
        fp = fopen(nversion, "wb");
        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, NULL);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, fp);
        res = curl_easy_perform(curl);
        curl_easy_cleanup(curl);
        fclose(fp);
    }
    printf("Updated to version %s.\n", nversion);
    return 0;
}

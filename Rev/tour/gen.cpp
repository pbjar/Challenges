#include <bits/stdc++.h>
#define endl '\n'
#define eat cin
#define moo cout

using namespace std;

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

int dp[1<<21][20];

int32_t main(){
    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
    pq.push({0, {1, 0}});
    for(int i = 0; i < (1<<21); i++) for(int j = 0; j < 20; j++) dp[i][j] = 1e9;
    dp[1][0] = 0;
    while(!pq.empty()){
        auto t = pq.top();
        pq.pop();
        int d = t.first;
        int bm = t.second.first;
        int cur = t.second.second;
        if(dp[bm][cur] != d) continue;
        dp[bm][cur] = d;
        //moo << d << " " << bm << " " << cur << endl;
        for(int i = 0; i < 15; i++){
            int nbm = bm | (1<<i);
            int nd = d + cost[cur][i];
            if(dp[nbm][i] <= nd) continue;
            dp[nbm][i] = nd;
            pq.push({nd, {nbm, i}});
        }
    }
    moo << dp[(1<<15)-1][0] << endl;
    stack<pair<int, int>> ans;
    pair<int, int> cur = {(1<<15)-1, 0};
    while(cur != make_pair(1, 0)){
        for(int i = 0; i < 15; i++){
            if(!(cur.first & (1<<i))) continue;
            if(dp[cur.first][i] + cost[i][cur.second] == dp[cur.first][cur.second]){
                ans.push({i, cur.second});
                cur.second = i;
                break;
            }
            int nbm = cur.first & (~(1<<(cur.second)));
            if(dp[nbm][i] + cost[i][cur.second] == dp[cur.first][cur.second]){
                ans.push({i, cur.second});
                cur = {nbm, i};
                break;
            }
        }
    }
    int curcost = 0;
    while(!ans.empty()){
        moo << ans.top().first << ' ' << ans.top().second << endl;
        curcost += cost[ans.top().first][ans.top().second];
        moo << curcost << endl;
        ans.pop();
    }
}

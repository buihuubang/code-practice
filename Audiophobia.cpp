//Pypy or python will cause time limit on this idea

#include <cmath>
#include <queue>
#include <string>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

#define MAX 101

long int dist[MAX];
bool visited[MAX];

struct option {
    bool operator()(const std::pair<int, int> &a, const std::pair<int, int> &b) const
    {
        return a.second > b.second;
    }
};

int main(){
    int c, s, q, ans;
    int a, b;
    int case_count = 0;
    while (true){
        scanf("%d %d %d",&c, &s, &q);
        if (c == 0 && s == 0 && q == 0)
            break;
        std::vector<std::pair<int, int>> graph[MAX];
        for(int i = 0; i < s; i++){
            int w;
            scanf("%d %d %d", &a, &b, &w);
            graph[a].push_back(std::make_pair(b, w));
            graph[b].push_back(std::make_pair(a, w));
        }
        printf ("Case #%d\n", ++case_count);
        for(int i = 0; i < q; i++){
            scanf("%d %d", &a, &b);
            std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, option> pq;
            memset(dist, 1000000, sizeof(dist));
            memset(visited, false, sizeof(visited));
            ans = -1;
            pq.push(std::make_pair(a, 0));
            dist[a] = 0;
            int max_sound = 0;
            int v, w;
            while (!pq.empty()) {
                int u = pq.top().first;
                int uw = pq.top().second;
                pq.pop();
                if (visited[u]){
                    continue;
                }
                visited[u] = true;
                max_sound = std::max(max_sound, uw);
                if (u == b){
                    ans = max_sound;
                    break;
                }
                for(auto neighbor: graph[u]){
                    v = neighbor.first;
                    w = neighbor.second;
                    if (!visited[v] && dist[v] > w){
                        dist[v] = w;
                        pq.push(std::make_pair(v, w));
                    }
                }
            }
            if (ans != -1)
                std::cout << ans << std::endl;
            else
                std::cout << "no path" << std::endl;
        }
        std::cout << std::endl;
    }
}

/*

TEST CASE:

INPUT:
7 9 3
1 2 50
1 3 60
2 4 120
2 5 90
3 6 50
4 6 80
4 7 70
5 7 40
6 7 140
1 7
2 6
6 2
7 6 3
1 2 50
1 3 60
2 4 120
3 6 50
4 6 80
5 7 40
7 5
1 7
2 4
0 0 0

OUTPUT:
Case #1
80
60
60

Case #2
40
no path
80

*/
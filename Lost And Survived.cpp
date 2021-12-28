#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <list>
#include <set>
using namespace std;

const int maxn = 100000;
multiset<int>s;

int fa[maxn + 5],num[maxn + 5],Max=1,Min=1;

int findSet(int u){
    if(u!=fa[u])
        fa[u] = findSet(fa[u]);
    return fa[u];
}

void unionSet(int u, int v){
    int fau=findSet(u),fav=findSet(v);
    if (fau != fav){
        if (rand() % 2)
            swap(fau, fav);
        fa[fav] = fau;
        s.erase(s.find(num[fau]));
        s.erase(s.find(num[fav]));
        num[fau] += num[fav];
        s.insert(num[fau]);
        if (num[fau] > Max)
            Max = num[fau];
        Min = *s.begin();
    }
}

int main()
{
    int N,Q,u,v,i;
    scanf("%d%d",&N,&Q);
    for(i=1;i<=N;i++){
        fa[i]=i; num[i]=1;
        s.insert(1);
    }
    while(Q--){
        scanf("%d%d",&u,&v);
        if(findSet(u)!=findSet(v))
            unionSet(u,v);
        printf("%d\n",Max-Min);
    }
    return 0;
}

/*
TEST CASE:

INPUT:
5 3
1 2
2 3
5 4

OUTPUT:
1
2
1
*/
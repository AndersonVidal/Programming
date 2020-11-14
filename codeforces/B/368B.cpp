#include <bits/stdc++.h>
    
using namespace std;
    
int tam[100100],v[100100],cont[100100];
    
int main(){
    int n,m,x;
    cin>>n>>m;
    set<int> s;
    for(int i=0;i<n;i++){
        cin>>v[i];
        tam[v[i]]++;
        s.insert(v[i]);
    }
    int resp = s.size();
    for(int i=0;i<n;i++){
        tam[v[i]]--;
        cont[i] = resp;
        if(tam[v[i]] == 0){
            resp--;
        }
    }
    for(int i=0;i<m;i++){
        cin>>x;
        cout<<cont[x-1]<<endl;
    }
    return 0;
}
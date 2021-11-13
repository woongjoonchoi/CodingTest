#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <iostream>
using namespace std;

int solution(vector<vector<string>> clothes) {
    unordered_multimap<string , string> spy_map;
    unordered_set<string> cl;
    int answer = 1, temp=1;
    for(auto i : clothes)
    {
        spy_map.insert({i[1],i[0]});
        cl.insert(i[1]);
    }
    for(auto  i : cl)
    {
        cout<<i<<endl;
        // answer+=spy_map.count(i);
        // temp= temp * spy_map.count(i);
        answer = answer * (spy_map.count(i)+1);
    }
    // if(cl.size()!=1) answer= answer + temp;

    return answer-1;
}
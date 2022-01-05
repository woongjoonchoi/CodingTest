#include <string>
#include <vector>
#include <iostream>
#include <regex>
#include <sstream>
#include <algorithm>
#include <unordered_set>
using namespace std;

bool cmp(string  a, string b){
    return a.length()<b.length() ;
}

vector<int> solution(string s) {
    smatch match;
    regex re( "[{]((\\d,?)+)[}]" );
    regex re1(",");
    vector<int> answer;
    unordered_set<string> dx;
    vector<string>sk;
    string temp = s;
    while(regex_search(temp,match,re) ) {
        string k = regex_replace(match[1].str() , re1 , " ");
        sk.push_back(k);
        temp=match.suffix();   
    }
    sort(sk.begin(),sk.end(),cmp);
    for(auto k = sk.begin();k!=sk.end();k++){
        stringstream ss(*k);
        string tmp;
        while(ss>>tmp){
            if(dx.find(tmp)==dx.end()){
                dx.insert(tmp);
                answer.push_back(stoi(tmp));
            }    
        }
    }
    return answer;
}
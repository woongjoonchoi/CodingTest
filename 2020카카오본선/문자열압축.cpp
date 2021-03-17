#include <string>
#include <vector>
#include <iostream>
#include <regex>
#include <sstream>
#include <algorithm>
using namespace std;

int solution(string s) {
    // int answer=1;
    int ans=1010;
    string answer="";
    stringstream ss;
    for(int i = 1; i<s.length()/2+1 ; i++)
    {
        string x = "(\\w{"; x += to_string(i); x += "})" ;string k="";
        regex re(x);int count =0;
        x=regex_replace(s,re,"$1 ");
        vector<string> tmp;
        stringstream ss(x);
        while(ss>>k){    
            tmp.push_back(k);
            cout<<ss<<endl;
        }   
        for(auto it = tmp.begin();it!=tmp.end();it++){
            count++;
            if( (it<tmp.end()-1 && (*it) != *(it+1)) || it == tmp.end()-1  ){
                k="";
                if(count>1) k = to_string(count);
                answer+=k+(*it);
                count=0;
            }
        }
        ans=min(ans,int(answer.length()));
        answer="";;
    }
    if (s.length()==1) ans=1;
    return ans;
}
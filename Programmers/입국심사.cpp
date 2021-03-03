#include <string>
#include <vector>
#include<algorithm>
using namespace std;

// 09분36초: end를 다시정하는부분
long long solution(int n, vector<int> times) {
    unsigned long long answer = 0;
    
    // answer = 100000000000000;
    answer = n*(*max_element(times.begin(),times.end()));
    // int len = times.size();
    unsigned long long start  = 0;
    unsigned long long end = answer;
    while(start<=end)
    {

        unsigned long long mid = (start+end)/2;
        if(start == end) {
            answer = mid;
            break;
        }
        unsigned long long ti = 0;
        for(auto k : times){
            ti+= mid/k ;
        }
        if(ti>= n ) end = mid;
        else start = mid+1;
        
    }

    return answer;
}
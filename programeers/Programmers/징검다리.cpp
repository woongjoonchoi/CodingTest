#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(int distance, vector<int> rocks, int n) {
    int answer = distance ;
//  500000
    vector<int> dist;
    sort(rocks.begin(),rocks.end());
    dist.push_back(rocks.front());
    for(int  i = 0 ; i<rocks.size()-1;i++)
    {
        dist.push_back(rocks[i+1]-rocks[i]);
    }
    dist.push_back(distance - rocks.back());
    int start = 1 , end = distance , mid = 0 ;;
    while(start <= end)
    {
        // if(end-start <= 1)
        // {
        //     break;
        // }
        mid = (start+end)/2;
        int sum = 0 ;
        int count =dist.size()+1 , m = INT_MAX;
        for(auto c : dist)
        {
            if(sum<mid){
                sum+=c;
                count--;
            }
            else{

                m = min(sum,m);
                sum = c;
                // count++;
            }
        }
        if(count >= dist.size()-n) {
            start = mid + 1;
            answer = m;
        }
        else end = mid - 1;
    }
    // int sum = 0,count=0;
    // for(auto c : dist)
    // {
    //     if(sum+c<=start){
    //         sum+=c;
            
    //     }
    //     else{
    //         sum = c;
    //         count++;
    //     }
    // }
    // if(count>=dist.size()-n) answer = min(answer , start);
    // sum = 0,count=0;
    // for(auto c : dist)
    // {
    //     if(sum+c<=end){
    //         sum+=c;
            
    //     }
    //     else{
    //         sum = c;
    //         count++;
    //     }
    // }
    // if(count>=dist.size()-n) answer = min(answer , end);
    return answer;
}

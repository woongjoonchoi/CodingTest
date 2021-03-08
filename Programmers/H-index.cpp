#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    int num = -1 , c_size  = citations.size() , ind = -1,flag=0;
    if(c_size==1 && citations[0]>=1) return 1;
    
    sort(citations.begin(),citations.end());
    // if(citations[0]>1000) return 0;
    // int start = citations[0] , end = *(citations.end()-1);
    
    int start = 0 , end = c_size;
    
    while(start<=end )
    {
        int mid= (start+end)/2;
        if(mid>citations[c_size-1]) end = mid-1;
        for(int i = 0 ; i< c_size;i++) {
            
            if(mid<= citations[i]){
                
                ind = i;
                if(c_size-ind>=mid ){
                    start = mid+1;
                    answer= max(answer, mid);
                    flag=1;
                    break;
                }
                else{
                    end = mid-1;
                    break;
                    
                }
            }

        }
        // if(start==end)
        // {
        //     if(mid>citations[c_size-1])break;   
        // }       
    }


    return answer;
}
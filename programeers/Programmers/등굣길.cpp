#include <string>
#include <vector>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    int answer = 0;
    vector<vector<int>> dp(100,vector<int>(100,0));

    
    for(int i = 0; i<n;i++)
    {
        for(int j =0 ;j<m;j++){
            int flag = 0;
            if(!puddles.empty())
            {
                for(int c = 0 ; c<puddles.size();c++)
                {
                    if(puddles[c][0]-1 == j && puddles[c][1]-1 == i) {
                        flag = 1;
                        break;
                    }
                }                
            }

            if(flag == 1) dp[i][j] = 0;
            else{
                if(i==0 && j==0) dp[i][j]= 1 ;
                if(j!=0) dp[i][j] += dp[i][j-1] % 1000000007  ;
                if(i!=0) dp[i][j] += dp[i-1][j] % 1000000007 ;
                
            }
        }
    }
    
    return dp[n-1][m-1] % 1000000007 ;
}
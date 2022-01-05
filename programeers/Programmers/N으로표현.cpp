#include <string>
#include <vector>
#include<sstream>
#include<algorithm>
#include<iostream>
using namespace std;



int solution(int N, int number) {
    int answer = 0;
    vector<vector<int>> subproblem(8);
    subproblem[0].push_back(N);
    for(int i =1 ; i< 8;i++)
    {
        string k = to_string(subproblem[i-1][0]);
        k+=to_string(N);
        int t = 0;
        stringstream ss(k);
        ss>>t;
        subproblem[i].push_back(t);
        for(int j = 0; j<i;j++)
        {
            for(int m = 0;m<subproblem[i-j-1].size();m++)
            {
                for(int n = 0;n<subproblem[j].size();n++)
                {
                    subproblem[i].push_back(subproblem[i-j-1][m]+subproblem[j][n]);
                    subproblem[i].push_back(subproblem[i-j-1][m]-subproblem[j][n]);
                    subproblem[i].push_back(subproblem[i-j-1][m]*subproblem[j][n]);
                    if(subproblem[j][n]!=0)subproblem[i].push_back(subproblem[i-j-1][m]/subproblem[j][n]);
                }
            }
        }
        if(find(subproblem[i].begin(),subproblem[i].end(),number)!=subproblem[i].end()) {
            answer = i;
            break;
        }
        // find(subproblem[i].beign(),subproblem[i].end(),N);

    }
    if(answer==0) answer= -1;
    else answer+=1;
    if (N==number) answer = 1;
    return answer;

}
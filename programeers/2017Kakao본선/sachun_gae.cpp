#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.


typedef struct 
{
    int x;
    int y;
}Point;
string solution(int m, int n, vector<string> board) {
    string answer = "";
    char cha = 'A';
    for(int i = 0;i<26;i++){
        cha = 'A' + i;
        int flag0 = 0;
        vector<Point> point;
        for(int k = 0 ;k<m;k++){
            for(int j = 0;j<n;j++){
                if(board[k][j] == cha){
                    Point p1;
                    p1.x = k;
                    p1.y = j;
                    point.push_back(p1);
                }
                if(point.size()==2){
                    int flag = 0;
                    int min_x = min(point[0].x,point[1].x);
                    int max_x = max(point[0].x,point[1].x);
                    int min_y = min(point[0].y,point[1].y);
                    int max_y = max(point[0].y,point[1].y); 
                    for(int m = min_x ; m <= max_x ; m ++ ){
                        if(board[m][point[0].y] != '.'&& board[m][point[0].y] != cha ){
                            flag = 1;
                            break;
                        }
                    }
                    for(int m = min_y; flag != 1 && m <=max_y ;m++){
                        if(board[point[1].x][m] != '.'&&board[point[1].x][m] != cha ){
                            flag = 1;
                            break;
                        } 
                    }
                    if(flag==1){
                        flag = 0;
                        for(int m = min_y ; m <= max_y ; m ++ ){
                            if(board[point[0].x][m] != '.'&&board[point[0].x][m] != cha ){
                                flag = 1;
                                break;
                            }
                        }
                        for(int m = min_x; flag != 1 && m <=max_x ;m++){
                            if(board[m][point[1].y] != '.'&&board[m][point[1].y] != cha ){
                                flag = 1;
                                break;
                            } 
                        }
                    }
                    if(flag == 0){
                        board[point[0].x][point[0].y] = '.';
                        board[point[1].x][point[1].y] = '.';
                        answer+=cha;
                        flag0=1;
                    }
                    break;
                }
                if(flag0==1) break;
            }
            if(flag0 == 1) break;
        }
        if(i==25&&flag0==0) {
            printf("check");
            break;
        }
        else if (flag0==1) i = -1;
    }
    for(auto a : board){
        for(auto c: a){
            if(c != '.' && c!='*'){
                answer ="IMPOSSIBLE";
            }
        }
    }
    if (answer=="") answer= "IMPOSSIBLE";
    return answer;
}


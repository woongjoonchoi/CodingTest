#include <string>
#include <vector>
// 수정
using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    //x = a+b
    int x = (brown +4 )/2;

    int a = 0;
    for(int b = 1 ;b < x;b++)
    {
        if(brown + yellow == (x-b) * b ){
            a  = x-b;
            break;
        } 
    }
    answer.push_back(a);
    answer.push_back(x-a);
    return answer;
}
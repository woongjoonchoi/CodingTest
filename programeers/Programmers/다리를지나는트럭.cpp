#include <string>
#include <vector>
#include <queue>
using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
	int answer = 1, weight_sum = 0;
	queue<int> road;
	queue<int> wait_truck;
	queue<int> in_time;
	vector<int>::iterator iter;
	for (iter = truck_weights.begin(); iter != truck_weights.end(); iter++)
	{
		wait_truck.push(*iter);
	}

	for (; !wait_truck.empty() || !road.empty(); answer++)
	{
		if (!in_time.empty() && answer-in_time.front()==bridge_length)
		{
			answer = in_time.front() + bridge_length;
			weight_sum -= road.front();
			road.pop();
			in_time.pop();
		}

		if (!wait_truck.empty() && weight_sum + wait_truck.front() <= weight)
		{
			road.push(wait_truck.front());
			weight_sum += wait_truck.front();
			wait_truck.pop();
			in_time.push(answer);
		}

	}

	return answer - 1;
}
#include <iostream>
#include <unordered_map>
using namespace std;

// 1742. 盒子中小球的最大数量
int sumOfValue(int num)
{
    int remainder;
    int sum = 0;
    while (num>0)
    {
        sum += (num % 10);
        num /= 10;
    }
    return sum;
}
int countBalls(int lowLimit, int highLimit)
{
    int box[100] = {0};
    int max=0;
    for (int i = lowLimit; i <= highLimit; i++)
    {
        int sum = sumOfValue(i);
        box[sum]++;
        if (box[sum]>max)
        {
            max=box[sum];
        }
    }
    return max;
}

int main(int, char**) {
    int ret = countBalls(19,28);
    cout<<ret<<endl;
}

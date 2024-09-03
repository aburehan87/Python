#include <iostream>
#include <climits>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int arr[n];

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    int MaxNo = 0;
    int MinNo = INT_MAX;

    for (int i = 0; i < n; i++)
    {
        if (arr[i] > MaxNo)
        {
            MaxNo = arr[i];
        }
        if (arr[i] < MinNo)
        {
            MinNo = arr[i];
        }
    }

    cout << "Maximun Number is:" << MaxNo << " ";
    cout << "Minimum Number is:" << MinNo << " ";

    return 0;
}

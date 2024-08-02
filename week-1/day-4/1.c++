Question Name: Suffix Sum

#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;  // Read the size of the array
    
    vector<int> arr(N);
    for (int i = 0; i < N; ++i) {
        cin >> arr[i];  // Read each element into the array
    }

    vector<int> suffixSum(N);
    
    // Compute suffix sums
    suffixSum[N - 1] = arr[N - 1];  // The last element is the same in both arrays
    for (int i = N - 2; i >= 0; --i) {
        suffixSum[i] = suffixSum[i + 1] + arr[i];
    }

    // Print the suffix sum array
    for (int i = 0; i < N; ++i) {
        cout << suffixSum[i] << " ";
    }
    cout << endl;

    return 0;
}

Question Name: Subarrays 


#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }
    
    // Generate and print all subarrays
    for (int start = 0; start < n; ++start) {
        for (int end = start; end < n; ++end) {
            for (int i = start; i <= end; ++i) {
                cout << arr[i] << " ";
            }
            cout << endl;
        }
    }
    
    return 0;
}

Question Name: Selection Sort

#include <iostream>
#include <vector>

using namespace std;

// Function to perform selection sort
void selectionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; ++i) {
        // Assume the minimum is the first element
        int minIndex = i;
        // Find the index of the minimum element in the remaining unsorted portion
        for (int j = i + 1; j < n; ++j) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        // Swap the found minimum element with the first element
        if (minIndex != i) {
            swap(arr[i], arr[minIndex]);
        }
    }
}

int main() {
    int N;
    cin >> N;  // Read the size of the array

    vector<int> arr(N);
    for (int i = 0; i < N; ++i) {
        cin >> arr[i];  // Read each element into the array
    }

    // Perform selection sort
    selectionSort(arr);

    // Print the sorted array
    for (int i = 0; i < N; ++i) {
        cout << arr[i]<<” “;
    }
    cout << endl;

    return 0;
}


Question Name: Bubble Sort


#include <iostream>
#include <vector>

using namespace std;

// Function to perform bubble sort
void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    bool swapped;
    for (int i = 0; i < n - 1; ++i) {
        swapped = false;
        for (int j = 0; j < n - i - 1; ++j) { // Corrected the loop boundary
            if (arr[j] > arr[j + 1]) { // Removed misplaced semicolon
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        // If no elements were swapped, break the loop
        if (!swapped) {
            break;
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

    // Perform bubble sort
    bubbleSort(arr);

    // Print the sorted array
    for (int i = 0; i < N; ++i) {
        cout << arr[i]; // Corrected missing semicolon
    }
    cout << endl; // Corrected missing semicolon

    return 0;
}

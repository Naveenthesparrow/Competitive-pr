Question Name: Insertion Sort


#include <iostream>
#include <vector>

using namespace std;

// Function to perform insertion sort
void insertionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; ++i) {
        int key = arr[i];
        int j = i - 1;
        
        // Move elements of arr[0..i-1], that are greater than key,
        // to one position ahead of their current position
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

int main() {
    int N;
    cin >> N;  // Read the size of the array

    vector<int> arr(N);
    for (int i = 0; i < N; ++i) {
        cin >> arr[i];  // Read each element into the array
    }

    // Perform insertion sort
    insertionSort(arr);

    // Print the sorted array
    for (int i = 0; i < N; ++i) {
        cout << arr[i]<<” “;
    }
    cout << endl;

    return 0;
}

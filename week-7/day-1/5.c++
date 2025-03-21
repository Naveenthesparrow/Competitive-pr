Question Name: Counting Alphabets, Digits and Special Characters

#include <iostream>
#include <string>

using namespace std;

int main() {
    string S;
    getline(cin, S);  // Read the input string including spaces

    int alphabets = 0, digits = 0, specialChars = 0;

    for (char c : S) {
        if (isalpha(c)) {
            ++alphabets;
        } else if (isdigit(c)) {
            ++digits;
        } else {
            ++specialChars;
        }
    }

    cout << alphabets << " " << digits << " " << specialChars << endl;

    return 0;
}

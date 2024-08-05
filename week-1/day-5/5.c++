Question Name: Anagrams

#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

bool areAnagrams(string str1, string str2) {
    // If the lengths of the strings are not equal, they cannot be anagrams
    if (str1.length() != str2.length()) {
        return false;
    }
    
    // Sort both strings
    sort(str1.begin(), str1.end());
    sort(str2.begin(), str2.end());
    
    // Compare the sorted strings
    return str1 == str2;
}

int main() {
    string str1, str2;
    
    cin >> str1 >> str2;
    
    if (areAnagrams(str1, str2)) {
        cout << "Anagrams" << endl;
    } else {
        cout << "Not Anagrams" << endl;
    }
    
    return 0;
}


class Playlist {
private:
    std::string name;
    std::vector<Song> songs;

public:
    Playlist(const std::string& playlistName) : name(playlistName) {}

    // Using the `this` pointer to set the name
    void setName(const std::string& name) {
        this->name = name;
    }

    void addSong(const Song& song) {
        songs.push_back(song);
        std::cout << "Song added to playlist." << std::endl;
    }

    void showPlaylist() const {
        std::cout << "Playlist: " << name << std::endl;
        for (const auto& song : songs) {
            song.displayInfo();
            std::cout << "------" << std::endl;
        }
    }
};

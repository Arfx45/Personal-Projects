#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
using namespace std;

int main() {
    unordered_map<string, string> rpsfGame;
    rpsfGame["Rock"] = "Paper";
    rpsfGame["Paper"] = "Scissors";
    rpsfGame["Scissors"] = "Rock";
    rpsfGame["Fox"] = "Foxen";

    int N;
    cin >> N;
    cin.ignore(); // ignore newline character

    vector<string> inps(N);
    for (int s = 0; s < N; s++) {
        getline(cin, inps[s]);
    }

    vector<string> outs;
    for (string i : inps) {
        if (i.compare("Foxen") == 0) {
            break;
        } else {
            outs.push_back(rpsfGame[i]);
        }
    }

    for (string j : outs) {
        cout << j << endl;
    }

    return 0;
}

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:

    // calc1: longest contiguous block of same character
    int calc1(const string& s) {
        int res = 0;
        int i = 0, n = s.length();

        while (i < n) {
            int j = i + 1;
            while (j < n && s[j] == s[i]) {
                j++;
            }
            res = max(res, j - i);
            i = j;
        }

        return res;
    }

    // calc2: longest substring containing only a & b
    // where counts of a and b are balanced
    int calc2(const string& s, char a, char b) {
        int res = 0;
        int i = 0, n = s.length();

        while (i < n) {

            // skip characters not a or b
            while (i < n && s[i] != a && s[i] != b) {
                i++;
            }

            unordered_map<int, int> pos;
            pos[0] = i - 1;   // difference 0 before starting
            int d = 0;

            while (i < n && (s[i] == a || s[i] == b)) {
                if (s[i] == a) d++;
                else d--;

                if (pos.find(d) != pos.end()) {
                    res = max(res, i - pos[d]);
                } else {
                    pos[d] = i;
                }

                i++;
            }
        }

        return res;
    }

    // calc3: longest substring where
    // count(a) = count(b) = count(c)
    int calc3(const string& s) {
        unordered_map<pair<int,int>, int, 
            function<size_t(pair<int,int>)>> pos(
                0, 
                [](pair<int,int> p) {
                    return hash<long long>()(
                        (static_cast<long long>(p.first) << 32) ^ p.second
                    );
                }
            );

        pos[{0, 0}] = -1;

        unordered_map<char, int> cnt;
        int res = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s[i];
            cnt[c]++;

            pair<int,int> key = {
                cnt['a'] - cnt['b'],
                cnt['b'] - cnt['c']
            };

            if (pos.find(key) != pos.end()) {
                res = max(res, i - pos[key]);
            } else {
                pos[key] = i;
            }
        }

        return res;
    }

    int longestBalanced(string s) {
        int x = calc1(s);

        int y = max({
            calc2(s, 'a', 'b'),
            calc2(s, 'b', 'c'),
            calc2(s, 'a', 'c')
        });

        int z = calc3(s);

        return max({x, y, z});
    }
};

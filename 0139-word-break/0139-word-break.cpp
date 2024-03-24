#include <unordered_map>
#include <unordered_set>
class Solution {
public:
   bool wordBreak(std::string s, std::vector<std::string>& wordDict) {
        std::unordered_set<std::string> dict(wordDict.begin(), wordDict.end());
        std::unordered_map<int, bool> memo; 
        return wordBreakHelper(s, 0, dict, memo);
    }
    
    bool wordBreakHelper(const std::string& s, int start, const std::unordered_set<std::string>& dict, std::unordered_map<int, bool>& memo) {
        if (start == s.length()) {
            return true; 
        }
        
        if (memo.find(start) != memo.end()) {
            return memo[start];
        }
        
        for (int end = start + 1; end <= s.length(); ++end) {
            std::string substring = s.substr(start, end - start);
            if (dict.find(substring) != dict.end() && wordBreakHelper(s, end, dict, memo)) {
                return memo[start] = true;
            }
        }
        
        return memo[start] = false;
    }
};
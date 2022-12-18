//https://leetcode.com/problems/longest-common-prefix/solutions/
// 14. Longest Common Prefix

#include <string> 
#include <vector> // for std::vector
#include <iostream> // for std::cout
#include <algorithm> // for std::sort
using namespace std;
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n = strs.size();
        
        // Sort the vector
        sort(strs.begin(), strs.end());
        string ans = ""; // for storing answer
        
        string a = strs[0]; // after sorting first element
        string b = strs[n-1]; // after sorting last element
        
        // We can compare for first and last , since they are sorted
        // i < a.length() ==> common prefix we can select least word
        for(int i = 0; i < a.length(); i++){
            if(a[i] == b[i]){
                // If same add in answer
                ans += a[i];
            }else{
                break;
            }
        }
        return ans;
    }
};

int main()
{
    static vector<string> v;
    Solution Obj;
    string FinalAns;
    FinalAns = Obj.longestCommonPrefix(v = {"flower","flow","flight"});
    // FinalAns = Obj.longestCommonPrefix(v = {"dog","racecar","car"});
    if (FinalAns == "")
    {
        cout<<"There is no common prefix among the input strings";
    }
    else
    {
        cout << FinalAns;
    }
}
#
# @lc app=leetcode id=2423 lang=python3
#
# [2423] Remove Letter To Equalize Frequency
#

# @lc code=start
from collections import Counter
class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq_map = Counter(word)

        # Count the frequency of frequencies
        freq_count = Counter(freq_map.values())

        # If there's only one distinct frequency, return True
        if len(freq_count) == 1:
            return True

     
        if len(freq_count) == 2 and (1 in freq_count.values()):
            min_freq, max_freq = sorted(freq_count.keys())
            return (max_freq - min_freq == 1 and freq_count[max_freq] == 1) or (min_freq == 1 and freq_count[min_freq] == 1)

        # If there are more than two distinct frequencies, it's not possible
        return False
# @lc code=end


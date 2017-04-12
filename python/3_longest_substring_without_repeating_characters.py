class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            raise Exception('invalid input')
        left = 0
        right = 0
        max = 0
        visited = {}
        while right < len(s):
            c = s[right]
            if c not in visited or left > visited[c]:
                max = right-left+1 if right-left+1 > max else max
                visited[c] = right
            else:
                left = visited[c]+1
                visited[c] = right
            right += 1
        return max

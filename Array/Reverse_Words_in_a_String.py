class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Split the string into words and reverse in one line, then join
        # return ' '.join(s.split()[::-1])
        
        # or
        
        # Split the string into words, filter out empty strings
        words = s.split()
        # Reverse the list of words
        words.reverse()
        # Join the words with a single space and return
        return ' '.join(words)


solution = Solution()
input_str1 = "the sky is blue"
output1 = solution.reverseWords(input_str1)
print("Output:", output1)  # Output: "blue is sky the"

# Test case 2
input_str2 = "  hello world  "
output2 = solution.reverseWords(input_str2)
print("Output:", output2)  # Output: "world hello"

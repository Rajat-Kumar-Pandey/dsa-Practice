class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Split the string by spaces
        w = s.split(' ')
        # Reverse each word in the list
        r_w = [word[::-1] for word in w]
        # Join the reversed words back into a single string
        return ' '.join(r_w)

# Example usage
solution = Solution()

# Test case 1
input_str1 = "Let's take LeetCode contest"
output1 = solution.reverseWords(input_str1)
print("Output:", output1)  # Output: "s'teL ekat edoCteeL tsetnoc"

# Test case 2
input_str2 = "Mr Ding"
output2 = solution.reverseWords(input_str2)
print("Output:", output2)  # Output: "rM gniD"

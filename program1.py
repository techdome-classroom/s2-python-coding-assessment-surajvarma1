# Solution code
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Mapping of closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in bracket_map:
                # Pop the topmost element from the stack if it exists, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the mapped opening bracket matches the top of the stack
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, so push onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets were matched correctly
        return not stack

# Test code
# import unittest

# class TestSolution(unittest.TestCase):
#     def setUp(self):
#         self.solution = Solution()

#     def test_valid_parentheses(self):
#         self.assertTrue(self.solution.isValid("()"))
#         self.assertTrue(self.solution.isValid("()[]{}"))
#         self.assertTrue(self.solution.isValid("{[()]}"))

#     def test_invalid_parentheses(self):
#         self.assertFalse(self.solution.isValid("(]"))
#         self.assertFalse(self.solution.isValid("([)]"))

#     def test_empty_string(self):
#         self.assertTrue(self.solution.isValid(""))

#     def test_mixed_parentheses(self):
#         self.assertFalse(self.solution.isValid("(){"))

# if __name__ == '__main__':
#     unittest.main(argv=['first-arg-is-ignored'], exit=False)












    



  


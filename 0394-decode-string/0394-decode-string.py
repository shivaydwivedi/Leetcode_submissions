class Solution:
    def decodeString(self, s: str) -> str:
        # num stack
        stack_num = []
        # str stack
        stack_str = []
        # string to keep track of the characters
        curr_str = ''
        # repeated number
        curr_num = 0
        # scan the string
        for c in s:
            # if character is a digit
            if c.isdigit():
                curr_num = curr_num*10 + int(c)
            # if character is opening bracket
            elif c == '[':
                # add current string to string stack
                stack_str.append(curr_str)
                # add current number to num stack
                stack_num.append(curr_num)
                # rest current string and number 
                curr_str = ""
                curr_num = 0
            # if character is a letter
            elif c.isalpha():
                # add it to the current string
                curr_str += c
            # if character is closing bracket
            elif c == ']':
                # pop the latest num for num stack and store it as repeat_count
                repeat_count = stack_num.pop()
                # pop string from string stack and store it in prev string
                prev_str = stack_str.pop()
                # build the new string
                curr_str = prev_str + curr_str*repeat_count
        # return the final current string
        return curr_str
        
class Solution:
    def compress(self, chars: List[str]) -> int:
        # initialize pointers
        read = 0
        write = 0
        # iterate through the array
        while read < len(chars):
            current_char = chars[read]
            count = 0
            # count how many times current_char repeats
            while read < len(chars) and chars[read] == current_char:
                read += 1
                count += 1
            # write the char
            chars[write] = current_char
            write += 1
            # if repeated more than once 
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

        return write
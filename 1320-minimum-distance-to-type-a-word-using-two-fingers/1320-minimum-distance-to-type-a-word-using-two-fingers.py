class Solution:
    def minimumDistance(self, word: str) -> int:
        """
        Calculate minimum distance to type a word using two fingers on a keyboard.
        The keyboard layout is A-Z arranged in a 6x5 grid (last row has 2 letters).
        """
      
        def calculate_distance(char1: int, char2: int) -> int:
            """
            Calculate Manhattan distance between two characters on the keyboard.
          
            Args:
                char1: First character index (0-25 for A-Z)
                char2: Second character index (0-25 for A-Z)
          
            Returns:
                Manhattan distance between the two positions
            """
            row1, col1 = divmod(char1, 6)
            row2, col2 = divmod(char2, 6)
            return abs(row1 - row2) + abs(col1 - col2)
      
        word_length = len(word)
      
        # dp[i][left_finger][right_finger] represents minimum distance after typing
        # word[0:i+1] with left finger at position left_finger and right finger at right_finger
        dp = [[[float('inf')] * 26 for _ in range(26)] for _ in range(word_length)]
      
        # Initialize first character - can be typed by either finger with 0 cost
        first_char_index = ord(word[0]) - ord('A')
        for finger_pos in range(26):
            dp[0][first_char_index][finger_pos] = 0  # Left finger typed first char
            dp[0][finger_pos][first_char_index] = 0  # Right finger typed first char
      
        # Process each subsequent character
        for i in range(1, word_length):
            prev_char_index = ord(word[i - 1]) - ord('A')
            curr_char_index = ord(word[i]) - ord('A')
            distance_between_chars = calculate_distance(prev_char_index, curr_char_index)
          
            for other_finger in range(26):
                # Case 1: Same finger that typed previous character types current character
                # Left finger was at prev_char, moves to curr_char
                dp[i][curr_char_index][other_finger] = min(
                    dp[i][curr_char_index][other_finger],
                    dp[i - 1][prev_char_index][other_finger] + distance_between_chars
                )
                # Right finger was at prev_char, moves to curr_char
                dp[i][other_finger][curr_char_index] = min(
                    dp[i][other_finger][curr_char_index],
                    dp[i - 1][other_finger][prev_char_index] + distance_between_chars
                )
              
                # Case 2: The other finger (not at prev_char) types current character
                if other_finger == prev_char_index:
                    for previous_position in range(26):
                        distance_to_current = calculate_distance(previous_position, curr_char_index)
                        # Left finger moves from previous_position to curr_char
                        dp[i][curr_char_index][other_finger] = min(
                            dp[i][curr_char_index][other_finger],
                            dp[i - 1][previous_position][prev_char_index] + distance_to_current
                        )
                        # Right finger moves from previous_position to curr_char
                        dp[i][other_finger][curr_char_index] = min(
                            dp[i][other_finger][curr_char_index],
                            dp[i - 1][prev_char_index][previous_position] + distance_to_current
                        )
      
        # Find minimum distance among all valid final states
        last_char_index = ord(word[-1]) - ord('A')
      
        # Minimum when left finger is at last character
        min_left_finger = min(dp[word_length - 1][last_char_index])
      
        # Minimum when right finger is at last character
        min_right_finger = min(dp[word_length - 1][j][last_char_index] for j in range(26))
      
        return int(min(min_left_finger, min_right_finger))
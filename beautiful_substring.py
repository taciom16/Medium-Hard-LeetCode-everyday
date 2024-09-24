class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        max_length = 0
        current_length = 0
        current_vowel_index = -1
        vowel_order = ['a', 'e', 'i', 'o', 'u']

        for char in word:
            if current_vowel_index == -1:
                if char == 'a':
                    current_vowel_index = 0
                    current_length = 1
            else:
                if char == vowel_order[current_vowel_index]:
                    current_length += 1
                    if current_vowel_index == 4:
                        max_length = max(max_length, current_length)

                elif current_vowel_index < 4 and char == vowel_order[current_vowel_index + 1]:
                    current_vowel_index += 1
                    current_length += 1
                    if current_vowel_index == 4:
                        max_length = max(max_length, current_length)
                elif char == 'a':
                    current_vowel_index = 0
                    current_length = 1

                else:
                    current_vowel_index = -1
                    current_length = 0

        return max_length

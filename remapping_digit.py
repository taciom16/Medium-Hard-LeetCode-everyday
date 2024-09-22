class Solution:
    def minMaxDifference(self, number: int) -> int:
        number_stringfied = str(number)

        highest_number = number_stringfied
        lowest_number = number_stringfied

        for digits in range(len(number_stringfied)):
            if number_stringfied[digits] != '9':
                highest_number = ''.join(map(lambda x: "9" if x == number_stringfied[digits] else x, number_stringfied))
                break

        for digits in range(len(number_stringfied)):
            if number_stringfied[digits] != '0':
                lowest_number = ''.join(map(lambda x: "0" if x == number_stringfied[digits] else x, number_stringfied))
                break
        solution = int(highest_number) - int(lowest_number)
        return solution

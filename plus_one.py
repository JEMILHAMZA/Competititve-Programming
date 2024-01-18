class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        concatenated_string = ''.join(map(str, digits))
        result_integer = int(concatenated_string)+1
        num_str = str(result_integer)

        digit_list = [int(digit) for digit in num_str]

        return digit_list


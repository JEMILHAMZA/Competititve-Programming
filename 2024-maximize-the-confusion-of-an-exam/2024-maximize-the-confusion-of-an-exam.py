class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxConsecutiveChar(char):
            left = 0
            max_len = 0
            count = 0

            for right in range(len(answerKey)):
                if answerKey[right] != char:
                    count += 1

                while count > k:
                    if answerKey[left] != char:
                        count -= 1
                    left += 1

                max_len = max(max_len, right - left + 1)

            return max_len

       
        return max(maxConsecutiveChar('T'), maxConsecutiveChar('F'))
        
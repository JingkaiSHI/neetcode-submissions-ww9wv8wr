class Solution:
    def compress(self, chars: List[str]) -> int:
        result = 0
        cur_rep = 0
        cur_element = None
        for i in range(len(chars)):
            if not cur_element:
                cur_element = chars[i]
                cur_rep = 1
            else:
                if chars[i] == cur_element:
                    cur_rep += 1
                else:
                    chars[result] = cur_element
                    result += 1
                    if cur_rep > 1:
                        reps = str(cur_rep)
                        for digit in reps:
                            chars[result] = digit
                            result += 1
                    cur_element = chars[i]
                    cur_rep = 1

        if cur_element is not None:
            chars[result] = cur_element
            result += 1
            if cur_rep > 1:
                for digit in str(cur_rep):
                    chars[result] = digit
                    result += 1
        return result
        
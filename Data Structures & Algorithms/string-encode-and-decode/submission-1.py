class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_result = ""
        for word in strs:
            encoded_result += str(len(word)) + "#" + word
        return encoded_result

    def decode(self, s: str) -> List[str]:
        # how to decode:
        # maintain a pointer ptr in a while loop
        # - in case of a number: 
        #   - we are likely looking at a word, but to make sure that they are followed by the pound key
        #   - logic goes as following:
        #       - if cur character is a number, mark current start of the number index i, mark seen_number as True, ptr += 1
        # - in case of a pound key: 
        #   - if seen_number = True, decode length the current word, add cur_word as s[i:i + x], add to list, reset word
        # - in case of other character:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            result.append(s[i:j])
            i = j
        return result

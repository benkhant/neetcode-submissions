class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for string in strs:
            encode += str(len(string)) + '#' + string
        return encode

    # Time: O(m + n)
    # Space: O(m + n), where m is the sum of lengths of all strings and n is the number of strings

    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            decode.append(s[j + 1:j + 1 + length])
            i = j + length + 1
        return decode

    # Time: O(m + n)
    # Space: O(m + n), where m is the sum of lengths of all strings and n is the number of strings


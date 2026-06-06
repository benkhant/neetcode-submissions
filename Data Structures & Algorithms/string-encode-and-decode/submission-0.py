class Solution:

    def encode(self, strs: List[str]) -> str:

        # loop thr the list
        # create an empty string
        # add every string to the empty string

        encoded_string = ""
        for char in strs:
            encoded_string += str(len(char)) + "#" + char
        return encoded_string

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res



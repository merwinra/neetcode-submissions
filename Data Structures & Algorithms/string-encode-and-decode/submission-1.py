class Solution:
    __DELIMITER: str = "#"

    def encode(self, strs: List[str]) -> str:
        res = ""
        for _str in strs:
            # note: # needs to come after len(_str) 
            # because utf-8 can contain numbers
            res += f"{len(_str)}#{_str}"
        return res


    def decode(self, s: str) -> List[str]:
        res = []

        ptr = 0
        while ptr < len(s):
            word_len = 0
            while s[ptr].isdigit():
                word_len *= 10
                word_len += int(s[ptr])
                ptr += 1
            
            ptr += 1 # increment to skip the #

            res.append(s[ptr:ptr + word_len:1])
            ptr += word_len

        return res
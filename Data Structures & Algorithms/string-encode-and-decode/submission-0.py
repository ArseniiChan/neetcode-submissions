class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            n = len(i)
            encoded_string += (str(n) + "#" + i)
        return encoded_string;

    def decode(self, s: str) -> List[str]:
        strs = [] #create an array 
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
                 # j is now at '#'
            length = int(s[i:j]) 
            word = s[j+1 : j+1+length]    # How do you extract the word?
            strs.append(word)
            i = j + 1 + length      # Where should i move to for the next iteration?
        return strs;

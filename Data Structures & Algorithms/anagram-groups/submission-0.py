class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_groups = {} #hashmap

        for word in strs:
            freq = [0] * 26 #create the freq for every letter of the alphabet

            for char in word:
                index = ord(char) - ord('a')
                freq[index] += 1
            
            key = tuple(freq)

            if key not in anagram_groups:
                anagram_groups[key] = []
            anagram_groups[key].append(word)

        return list(anagram_groups.values())
        
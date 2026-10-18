class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #pre list of strings

        #post groupAnagrams

        #create a dict 

        # go through the list and start adding to dict 

        # when you are going throught the list you check the dict and see if that value is in the dict if its not then add it.

        anag = {}

        for s in strs:
            key = "".join(sorted(s))
            if key not in anag:
                anag[key] = []
            anag[key].append(s)
        return list(anag.values())


        
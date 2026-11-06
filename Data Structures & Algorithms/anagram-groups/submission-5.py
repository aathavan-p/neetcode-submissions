class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            counter = [0] * 26
            for ch in word:
                idx = ord(ch)-ord('a')
                counter[idx]+=1
            key = tuple(counter)
            anagram_map[key].append(word)
        
        return list(anagram_map.values())
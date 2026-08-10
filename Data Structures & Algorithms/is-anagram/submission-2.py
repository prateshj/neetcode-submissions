class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        word_count1={}
        word_count2={}

        if len(s)!=len(t):

            return False

        for s1 in s:

            word_count1[s1]=1+ word_count1.get(s1,0)

        for t1 in t:

            word_count2[t1]=1+ word_count2.get(t1,0)

        return word_count1==word_count2


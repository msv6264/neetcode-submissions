class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       hashi1={}
       if len(s)!=len(t):
           return False
       for i in range(len(s)):
           hashi1[s[i]]=hashi1.get(s[i],0)+1
           hashi1[t[i]]=hashi1.get(t[i],0)-1
       return all(value==0 for value in hashi1.values())


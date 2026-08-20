class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       hashi1={}
       hashi2={}
       for i in range(len(s)):
           hashi1[s[i]]=hashi1.get(s[i],0)+1
       for j in range(len(t)):
           hashi2[t[j]]=hashi2.get(t[j],0)+1
       if hashi1==hashi2:
           return True
       return False


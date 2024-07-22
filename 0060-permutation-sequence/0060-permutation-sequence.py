class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def rec(k,l,ans,n):
            if(n==0):return
            combo=(math.factorial(n-1))
            element=k//combo
            mod=k%combo
            ans+=[l[element]]
            l.pop(element)
            rec(mod,l,ans,n-1)
            return ''.join(map(str, ans))
        l=[i for i in range(1,n+1)]
        return rec(k-1,l,[],n)

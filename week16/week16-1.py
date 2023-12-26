#"00111"想知道左邊幾個0,右邊幾個1 加起來最多
#for left in range(N-1)  0...left左邊 右邊;left+1...N-1
class Solution:
    def maxScore(self, s: str) -> int:
        N=len(s)#字串長度
        ans=0
        for left in range(N-1):
            now=0
            for i in range(N):
                if i<=left and s[i]=='0':now+=1
                if i>left and s[i]=='1':now+=1
            if now>ans:ans=now
        return ans
        
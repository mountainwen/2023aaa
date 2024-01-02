class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[[nums[0]]]#把最前面,最小的數字,放在兩層方括號裡
        repeat =0 #目前的nums[0]沒有重複
        N=len(nums)#有幾個數字
        for i in range(1,N):#想比較nums[i]vs. nums[i-1]是否相同
            if nums[i]==nums[i-1]:#這裡要處理,重複,相同,就repeat+=1
                repeat+=1
                if len(ans)<=repeat:#目前的層數不夠多
                    ans.append([])
            else:
                 repeat=0
            ans[repeat].append(nums[i])
        return ans
                
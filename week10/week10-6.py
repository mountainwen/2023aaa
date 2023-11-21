class Solution:
    def average(self, salary: List[int]) -> float:
        
        total=sum(salary)-max(salary)-min(salary)
        N=len(salary)-2#因為扣掉最大值,最小值,
        return total/N
  
        #return sum(salary)-max(salary)-min(salary) / (len(salary)-2)
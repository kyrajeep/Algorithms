class Solution:
    def jump(self, nums: List[int]) -> int:
        #BASE CASE: when index == n-1
        #variables: index, steps you can jump 
        table = {} #save intermediate results indexed by (index, step)
        result = 0
        def dp(index, steps, result):
            if index == n-1:
                return result #TODO:     check logic
            elif table[(index, steps)]:
                return table[(index, steps)]
            else:
                result += 1
                index = index + step
                dp[(index, steps)] = result
                for i in range(step):
                    dp[(index, i)] #TODO:check logic
        return dp(0, nums[0],result)
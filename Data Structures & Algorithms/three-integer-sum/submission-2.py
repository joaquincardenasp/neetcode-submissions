class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        output = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            while j < k:
                tmp = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                if tmp < 0:
                    j +=1
                elif tmp > 0:
                    k -=1
                else: 
                    output.append([sorted_nums[i],sorted_nums[j],sorted_nums[k]])
                    j += 1
                    k -= 1
                    while j < k and sorted_nums[j] == sorted_nums[j-1]:
                        j += 1
        return output
                    

        
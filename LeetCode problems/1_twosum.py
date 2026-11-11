

# Online Python - IDE, Editor, Compiler, Interpreter

'''
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

'''

nums = [2,7,11,15]

target = 9


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            #print('this is i: ',i)
            for j in range(i+1,len(nums)):
                test = nums[i] + nums[j]
                #print('this is j: ',j)
                #print('this is test: ' ,test)
                if test==target:
                    print('found target')
                    indices = [i,j]
                    return indices
                else:
                    continue
                    #print('no')
        #print('end of loop')



solver = Solution()
result = solver.twoSum(nums,target)
print(result)









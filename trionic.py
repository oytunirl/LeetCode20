from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        state = 0
        for x in range(1,len(nums)):
            if state == 0:
                if nums[x] == nums[x-1]:
                    return False
                elif nums[x] > nums[x-1]:
                    state = 1
                    continue
                else:
                    return False
            elif state == 1:
                if nums[x] == nums[x-1]:
                    return False
                elif nums[x] > nums[x-1]:
                    continue
                else:
                    state = 2
                    continue
            elif state == 2:
                if nums[x] == nums[x-1]:
                    return False
                elif nums[x] > nums[x-1]:
                    state = 3
                    continue
            elif state == 3:
                if nums[x] > nums[x-1]:
                    continue
                else:
                    return False
        
        return True if state == 3 else False
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    ret: List[int] = []
    chk = False
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                ret.append(i)
                ret.append(j)
                chk = True
            if chk:
                break
        if chk:
            break
    return ret

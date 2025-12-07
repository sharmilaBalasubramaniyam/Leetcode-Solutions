class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def res(x):
            m=bin(x)[2:]
            s=m[::-1]
            return int(s,2)
        return sorted(nums,key=lambda x:(res(x),x))

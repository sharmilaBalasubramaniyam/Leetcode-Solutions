class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        st=[]
        for n in nums:
            st.append(n)

            while len(st)>=2 and st[-1]==st[-2]:
                m=st.pop()
                st[-1]+=m
        return st
        

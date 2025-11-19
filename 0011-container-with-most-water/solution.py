class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        mw=0

        while l<=r:
            w=r-l
            ch=min(height[l],height[r])
            area=w*ch
            mw=max(mw,area)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return mw

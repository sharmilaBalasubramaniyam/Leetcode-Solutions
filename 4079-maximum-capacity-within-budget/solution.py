class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        
       
        # n=len(costs)
    
        # res=0

        # for i in range(n):
        #     if costs[i]<budget:
        #         res=max(res,capacity[i])
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if costs[i]+costs[j]<budget:
        #             res=max(res,capacity[i]+capacity[j])
        # return res

        #

        n=len(costs)
        ma=sorted(zip(costs,capacity))

        pref=[0]*n
        pref[0]=ma[0][1]

        for i in range(1,n):
            pref[i]=max(pref[i-1],ma[i][1])
        res=0

        for c,cap in ma:
            if c<budget:
                res=max(res,cap)

        co=[c for c,_ in ma]

        for i in range(n):
            c1,cap1=ma[i]
            r=budget-c1-1
            if r<0:
                continue
            j=bisect.bisect_right(co,r,0,i)-1
            if j>=0:
                res=max(res,cap1+pref[j])
        return res

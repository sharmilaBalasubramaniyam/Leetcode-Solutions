class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)<=2:
            return len(points)
        
        def fs(p1,p2):
            x1,y1=p1
            x2,y2=p2
            if x1-x2==0:
                return inf
            return (y1-y2)/(x1-x2)
        
        res=1
        for i,p1 in enumerate(points):
            sl=defaultdict(int)
            for j,p2 in enumerate(points[i+1:]):
                s=fs(p1,p2)
                sl[s]+=1
                res=max(sl[s],res)
        return res+1

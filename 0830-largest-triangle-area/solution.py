class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ma=0
        n=len(points)

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    ma=max(ma,
                    abs(
                        points[i][0] * (points[j][1]-points[k][1])+(points[j][0] * (points[k][1]-points[i][1])+points[k][0]*(points[i][1]-points[j][1]))
                    ))
        return ma/2

class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        cx,cy=center
        bq=-1
        bc=[-1,-1]
        for x,y,q in towers:
            dis=abs(x-cx)+abs(y-cy)
            if dis<=radius:
                if q>bq:
                    bq=q
                    bc=[x,y]
                elif q==bq:
                    if bc==[-1,-1] or [x,y]<bc:
                        bc=[x,y]
        return bc
        

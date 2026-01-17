class Solution:
    def minimumFlips(self, n: int, edges: List[List[int]], start: str, target: str) -> List[int]:
        g=[[] for _ in range(n)]
        for id,(u,v) in enumerate(edges):
            g[u].append((v,id))
            g[v].append((u,id))

        res=[]

        curr=list(map(int,start))

        def dfs(node,parent):
            for nt,idx in g[node]:
                if nt==parent:
                    continue
                dfs(nt,node)

                if curr[nt]!=int(target[nt]):
                    res.append(idx)
                    curr[nt]^=1
                    curr[node]^=1
        dfs(0,-1)

        for i in range(n):
            if curr[i]!=int(target[i]):
                return [-1]
        return sorted(res)
        

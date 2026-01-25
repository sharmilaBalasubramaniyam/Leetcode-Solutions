class Solution {
    List<Integer>[] g;
    int[] dp;
    int n;
    public int specialNodes(int n, int[][] edges, int x, int y, int z) {
        this.n=n;
        g=new ArrayList[n];
        for(int i=0;i<n;i++){
            g[i]=new ArrayList<>();
        }
        for(int[] e:edges){
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
                
        }

        int[] dx=cd(x);
        int[] dy=cd(y);
        int[] dz=cd(z);

        int res=0;

        for(int i=0;i<n;i++){
            int[] d={dx[i],dy[i],dz[i]};
            Arrays.sort(d);
            if (d[0]*d[0]+d[1]*d[1]==d[2]*d[2]){
                res++;
            }
        }
        return res;
    }

    private int[] cd(int s){
        dp=new  int[n];
        Arrays.fill(dp,-1);
        dfs(s,-1,0);
        return dp;
    }

    private void dfs(int u,int p,int d){
        dp[u]=d;
        for(int v:g[u]){
            if(v!=p){
                dfs(v,u,d+1);
            }
        }
    }
}

class Solution {
    public int maximumWealth(int[][] accounts) {
        int m=0;
        for(int[] cus:accounts){
            int sum=0;
            for(int mon:cus){
                sum+=mon;
            }
            m=Math.max(m,sum);
        }
        return m;
    }
}

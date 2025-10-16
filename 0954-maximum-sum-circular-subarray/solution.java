class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        int t=0;
        int ms=nums[0];
        int cm=0;
        int mis=nums[0];
        int cmi=0;

        for(int n:nums){
            cm=Math.max(n,cm+n);
            ms=Math.max(ms,cm);

            cmi=Math.min(n,cmi+n);
            mis=Math.min(mis,cmi);

            t+=n;
        }
        if(ms<0){
            return ms;
        }
        return Math.max(ms,t-mis);
    }
}

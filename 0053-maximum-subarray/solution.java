class Solution {
    public int maxSubArray(int[] nums) {
        int m=nums[0],sum=0;
        for(int n:nums){
        sum=Math.max(n,sum+n);
        m=Math.max(m,sum);
    }
    return m;
    }
}

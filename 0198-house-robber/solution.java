class Solution {
    public int rob(int[] nums) {
        if(nums.length==0) return 0;
        if(nums.length==1) return nums[0];

        int prev=nums[0];
        int prev1=Math.max(nums[0],nums[1]);
        int cur=prev1;

        for(int i=2;i<nums.length;i++){
            cur=Math.max(prev1,prev+nums[i]);
            prev=prev1;
            prev1=cur;
        }
        return cur;
    }
}

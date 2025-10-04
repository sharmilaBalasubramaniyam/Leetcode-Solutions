class Solution {
    public int maximumDifference(int[] nums) {
        int min=nums[0];
        int md=-1;
        for(int i=1;i<nums.length;i++){
            if(nums[i]>min){
                md=Math.max(md,nums[i]-min);
            }else{
                min=nums[i];
            }
        }
        return md;
    }
}

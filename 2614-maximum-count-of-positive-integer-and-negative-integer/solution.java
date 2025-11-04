class Solution {
    public int maximumCount(int[] nums) {
        int n=nums.length;
        int pc=0;
        int nc=0;
        for(int i=0;i<n;i++){
            if(nums[i]<0){
                nc++;
            }
            if(nums[i]>0){
                pc++;
            }
            if(nums[i]==0){
                continue;
            }
        }
        return Math.max(pc,nc);
    }
}

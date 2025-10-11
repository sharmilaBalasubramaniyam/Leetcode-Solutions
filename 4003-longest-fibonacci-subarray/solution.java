class Solution {
    public int longestSubarray(int[] nums) {
        int n=nums.length;
        if(n<2) return n;
        int l=2;
        int cl=2;

        for(int i=2;i<n;i++){
            if(nums[i]==nums[i-1]+nums[i-2]){
                cl++;
            }else{
                cl=2;
            }
            l=Math.max(l,cl);
        }
        return l;
    }
}

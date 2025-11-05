class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int n=nums.length;
        int ws=0;
        

        for(int i=0;i<k;i++){
            ws+=nums[i];
        }
        int ms=ws;

        for(int i=k;i<n;i++){
            ws+=nums[i]-nums[i-k];
            ms=Math.max(ms,ws);
        }
        return (double) ms/k;
    }
}

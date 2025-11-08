class Solution {
    public int evenNumberBitwiseORs(int[] nums) {
        int n=nums.length;
        int sum=0;
        for(int i=0;i<n;i++){
            if((nums[i]&1)==0){
                sum|=nums[i];
            }
        }
        return sum;
    }
}

class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int idx=0;idx<nums.length;idx++){
            for(int taridx=idx+1;taridx<nums.length;taridx++){
                if(nums[idx]+nums[taridx]==target){
                    return new int[]{idx,taridx};
                }
            }
        }
        return new int[]{};
    }
}

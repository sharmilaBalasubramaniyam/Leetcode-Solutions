import java.util.Arrays;

class Solution {
    public int triangleNumber(int[] nums) {
        Arrays.sort(nums);
        int n=nums.length;
        int c=0;

        for(int i=n-1;i>=2;i--){
            int s=0;
            int e=i-1;

            while(s<e){
                if(nums[s]+nums[e]>nums[i]){
                    c+=(e-s);
                    e--;
                }else{
                    s++;
                }
            }
        }
        return c;
    }
}

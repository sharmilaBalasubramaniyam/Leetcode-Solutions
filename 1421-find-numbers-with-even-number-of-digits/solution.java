class Solution {
    public int findNumbers(int[] nums) {
        int c=0;
        for(int num:nums){
            int d=0;
            while(num!=0){
                d++;
                num/=10;
            }
            if(d%2==0) c++;
        }
        return c;
    }
}

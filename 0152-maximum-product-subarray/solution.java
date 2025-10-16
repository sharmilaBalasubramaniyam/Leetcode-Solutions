class Solution {
    public int maxProduct(int[] nums) {
        int mp=nums[0];
        int mip=nums[0];
        int res=nums[0];

        for(int i=1;i<nums.length;i++){
            int c=nums[i];

            if(c<0){
                int temp=mp;
                mp=mip;
                mip=temp;
            }
            mp=Math.max(c,mp*c);
            mip=Math.min(c,mip*c);

            res=Math.max(res,mp);
        }
        return res;
    }
}

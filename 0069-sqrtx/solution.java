class Solution {
    public int mySqrt(int x) {
        if(x<2) return x;

        int l=1,r=x/2;
        int res=0;


        while(l<=r){
            int mid=l+(r-l)/2;
            long s=(long)mid*mid;

            if(s==x){
                return mid;
            }else if(s<x){
                res=mid;
                l=mid+1;
            }else{
                r=mid-1;
            }
        }
        return res;
    }
}

class Solution {
    public int largestAltitude(int[] gain) {
        int ma=0;
        int ca=0;
        for(int a:gain){
            ca+=a;
            ma=Math.max(ca,ma);
        }
        return ma;
    }
}

class Solution {
    public int hammingDistance(int x, int y) {
        int m=x^y;
        int c=0;
        while(m!=0){
            c+=m&1;
            m>>=1;
        }
        return c;
    }
}

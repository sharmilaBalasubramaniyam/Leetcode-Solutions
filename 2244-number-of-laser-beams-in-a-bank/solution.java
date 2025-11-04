class Solution {
    public int numberOfBeams(String[] bank) {
        int n=bank[0].length();
        int res=0,prev=0;
        for(String r:bank){
            int temp=0;
            for(int i=0;i<n;i++){
                temp+=(r.charAt(i)=='1')?1:0;
            }
            if(temp>0){
                res+=temp*prev;
                prev=temp;
            }
        }
        return res;
    }
}

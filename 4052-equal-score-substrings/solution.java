class Solution {
    public boolean scoreBalance(String s) {
        int n=s.length();
        int[] p=new int[n];
        p[0]=s.charAt(0)-'a'+1;

        for(int i=1;i<n;i++){
            p[i]=p[i-1]+(s.charAt(i)-'a'+1);
        }
            for(int i=1;i<n;i++){
            int l=p[i-1];
            int r=p[n-1]-p[i-1];
            if(l==r){
                return true;
            }
        }
        return false;
    }
}

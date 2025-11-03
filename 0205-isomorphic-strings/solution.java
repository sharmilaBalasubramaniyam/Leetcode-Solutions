class Solution {
    public boolean isIsomorphic(String s, String t) {
        int[] m=new int[256];
        int[] n=new int[256];
        for(int i=0;i<s.length();i++){
            char c1=s.charAt(i);
            char c2=t.charAt(i);
            if(m[c1]!=n[c2]) return false;
            m[c1]=i+1;
            n[c2]=i+1;
        }
        return true;
    }
}

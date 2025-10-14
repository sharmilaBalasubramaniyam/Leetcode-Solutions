class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs==null || strs.length==0) return "";

        String st=strs[0];
        int n=st.length();

        for(int i=0;i<n;i++){
            char c=st.charAt(i);
            for(int j=1;j<strs.length;j++){
                if(i>=strs[j].length()||strs[j].charAt(i)!=c){
                    return st.substring(0,i);

                }
            }

        }
        return st;
    }
}

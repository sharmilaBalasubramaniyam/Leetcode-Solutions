class Solution {
    public String simplifyPath(String path) {
        String[] pa=path.split("/");
        Stack<String> st=new Stack<>();
        for(String p:pa){
            if(p.equals("")||p.equals(".")){
                continue;
            }else if(p.equals("..")){
                if(!st.isEmpty()){
                    st.pop();
                }
            }else{
                st.push(p);
            }
        }
        return '/'+String.join("/",st);

    }
}

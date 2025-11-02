class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> st=new Stack<>();
        for(String o:operations){
            if(o.equals("C")){
                st.pop();
            }else if(o.equals("D")){
                st.push(st.peek()*2);
            }else if(o.equals("+")){
                int l=st.pop();
                int sl=st.peek();
                int sum=l+sl;
                st.push(l);
                st.push(sum);
            }else{
                st.push(Integer.parseInt(o));
            }
        }
        int tot=0;
        for(int s:st){
            tot+=s;
        }
        return tot;
    }
}

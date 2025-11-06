class Solution {
    public long removeZeros(long n) {
        String s=Long.toString(n).replace("0","");
        return Long.parseLong(s);


        // String s=Long.toString(n);
        // String r="";

        // for(int i=0;i<s.length();i++){
        //     if(s.charAt(i)=='0'){
        //         continue;
        //     }
        //     r+=s.charAt(i);
        // }
        // return Long.parseLong(r);
    }

    
}

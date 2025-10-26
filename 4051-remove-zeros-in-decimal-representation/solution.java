class Solution {
    public long removeZeros(long n) {
        
        String s=Long.toString(n).replace("0","");
        return Long.parseLong(s);
        
    
    }
    
}

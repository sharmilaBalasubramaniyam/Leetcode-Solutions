class Solution {
    public int myAtoi(String s) {
        if(s==null || s.isEmpty()) return 0;

        int i=0,n=s.length();
        while(i<n && s.charAt(i)==' ') i++;
        if(i==n) return 0;

        int sign=1;
        if(s.charAt(i)=='+' || s.charAt(i)=='-'){
            sign=(s.charAt(i)=='-')?-1:1;
            i++;
        }

        int num=0;
        int ma=Integer.MAX_VALUE;
        int mi=Integer.MIN_VALUE;
        while(i<n && Character.isDigit(s.charAt(i))){
            int d=s.charAt(i)-'0';
            if(num>(ma-d)/10)
            return (sign==1)?ma:mi;
        num=num*10+d;
        i++;
        }

    return num*sign;
    }
}

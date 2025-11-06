class Solution {
    public String reverseOnlyLetters(String s) {
        char[] rev=s.toCharArray();
        int l=0,r=rev.length-1;
        while(l<r){
            if(!Character.isLetter(rev[l])) l++;
            else if(!Character.isLetter(rev[r])) r--;
            else{
                char temp=rev[l];
                rev[l]=rev[r];
                rev[r]=temp;
                l++;
                r--;
            }
        }
        return new String(rev);
    }
}

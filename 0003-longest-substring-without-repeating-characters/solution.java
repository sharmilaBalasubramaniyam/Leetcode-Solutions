class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character,Integer> last=new HashMap<>();
        int l=0,ml=0;
        for(int r=0;r<s.length();r++){
            char ch=s.charAt(r);
            if(last.containsKey(ch) && last.get(ch)>=l){
                l=last.get(ch)+1;
            }
            last.put(ch,r);
            ml=Math.max(ml,r-l+1);
        }
        return ml;
    }
}

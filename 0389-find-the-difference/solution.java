class Solution {
    public char findTheDifference(String s, String t) {
        int ssum=0,tsum=0;

        for(char c:s.toCharArray()){
            ssum+=c;
        }
        for(char c:t.toCharArray()){
            tsum+=c;
        }
        return (char)(tsum-ssum);
    }
}

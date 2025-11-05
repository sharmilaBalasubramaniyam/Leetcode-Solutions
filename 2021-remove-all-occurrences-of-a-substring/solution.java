class Solution {
    public String removeOccurrences(String s, String part) {
       while(s.contains(part)){
        int o=s.indexOf(part);
        s=s.substring(0,o)+s.substring(o+part.length());
       }
       return s;
    }
}

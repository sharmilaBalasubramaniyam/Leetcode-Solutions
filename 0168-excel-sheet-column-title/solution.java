class Solution {
    public String convertToTitle(int columnNumber) {
        StringBuilder sb=new StringBuilder();

        while(columnNumber >0){
            columnNumber--;
            int r=columnNumber % 26;
            char l=(char)('A'+r);
            sb.append(l);
            columnNumber/=26;
        }
        return sb.reverse().toString();
    }
}

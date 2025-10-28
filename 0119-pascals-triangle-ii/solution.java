class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> r=new ArrayList<>();
        long v=1;

        for(int i=0;i<=rowIndex;i++){
            r.add((int)v);
            v=v*(rowIndex-i)/(i+1);    
        }
        return r;
    }
}

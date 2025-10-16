class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> tri=new ArrayList<>();
        for(int i=0;i<numRows;i++){
            List<Integer> r=new ArrayList<>();

            for(int j=0;j<=i;j++){
                if(j==0 || j==i){
                    r.add(1);
                }else{
                    int v=tri.get(i-1).get(j-1)+tri.get(i-1).get(j);
                    r.add(v);
                }
            }
            tri.add(r);
        }
        return tri;
    }
}

class Solution {
    public int findLucky(int[] arr) {
        int[] c=new int[501];

        for(int num:arr){
            c[num]++;
        }
        int l=-1;
        for(int i=1;i<=500;i++){
            if(c[i]==i){
                l=i;
            }
        }
        return l;
    }
}

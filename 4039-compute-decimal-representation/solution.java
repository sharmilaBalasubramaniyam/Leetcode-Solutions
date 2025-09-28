class Solution {
    public int[] decimalRepresentation(int n) {
        List<Integer> l=new ArrayList<>();
        int pow=1;
        while(n>0){
            int d=n%10;
            if(d!=0){
                l.add(d*pow);
            }
            n/=10;
            pow*=10;
        }

        int size=l.size();
        int[] arr=new int[size];
        for(int i=0;i<size;i++){
            arr[i]=l.get(size-1-i);
        }
        return arr;
    }
}

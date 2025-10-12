class Solution {
    public int sumDivisibleByK(int[] nums, int k) {
        Map<Integer,Integer> map=new HashMap<>();
      

        for(int i:nums){
            map.put(i,map.getOrDefault(i,0)+1);
        }
        int sum=0;
        boolean flag=false;
        for(Map.Entry<Integer,Integer> entry:map.entrySet()){
            int n=entry.getKey();
            int f=entry.getValue();
            if(f%k==0){
                sum+=n*f;
                flag=true;
            }
        }
        return flag?sum:0;
    }
}

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        boolean[] s=new boolean[nums.length+1];
        List<Integer> m=new ArrayList<>();
        for(int num:nums){
            s[num]=true;
        }
        for(int i=1;i<=nums.length;i++){
            if(!s[i]){
                m.add(i);
            }
        }
        return m;
    }
}

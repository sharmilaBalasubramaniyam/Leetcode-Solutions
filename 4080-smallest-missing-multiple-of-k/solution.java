class Solution {
    public int missingMultiple(int[] nums, int k) {
        Set<Integer> s=new HashSet<>();
        for(int n:nums){
            s.add(n);
        }
        int m=k;

        while(s.contains(m)){
            m+=k;
        }
        return m;
    }
}

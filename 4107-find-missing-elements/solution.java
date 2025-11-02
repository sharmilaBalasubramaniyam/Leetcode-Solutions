class Solution {
    public List<Integer> findMissingElements(int[] nums) {
        List<Integer> res=new ArrayList<>();
        if(nums==null || nums.length==0) return res;
        int min=Integer.MAX_VALUE;
        int max=Integer.MIN_VALUE;
        Set<Integer> s=new HashSet<>();
        for(int num:nums){
            min=Math.min(min,num);
            max=Math.max(max,num);
            s.add(num);
        }
        for(int i=min;i<=max;i++){
            if(!s.contains(i)){
                res.add(i);
            }
        }
        return res;
    }
}

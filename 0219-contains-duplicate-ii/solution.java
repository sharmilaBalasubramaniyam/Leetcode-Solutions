class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashSet<Integer> l=new HashSet<>();
        for(int i=0;i<nums.length;i++){
           if(l.contains(nums[i])) return true;
           l.add(nums[i]);
           if(l.size()>k){
            l.remove(nums[i-k]);
           }
        }
        return false;
    }
}

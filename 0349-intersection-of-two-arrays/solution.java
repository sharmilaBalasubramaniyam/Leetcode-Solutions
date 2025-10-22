class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> s=new HashSet<>();
        for(int x:nums1) s.add(x);
        Set<Integer> m=new HashSet<>();
        for(int y:nums2) 
        if(s.contains(y)) 
        m.add(y);

        int[] res=new int[m.size()];
        int i=0;
        for(int n:m) res[i++]=n;
        return res;
    }
}

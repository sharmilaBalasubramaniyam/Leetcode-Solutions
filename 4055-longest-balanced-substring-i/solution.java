class Solution {
    public int longestBalanced(String s) {
        int n=s.length();
        int m=0;

        for(int i=0;i<n;i++){
            int[] arr=new int[26];
            for(int j=i;j<n;j++){
                arr[s.charAt(j)-'a']++;
                int sm=0;
                boolean flag=true;
                for(int k=0;k<26;k++){
                    if(arr[k]>0){
                        if(sm==0){
                            sm=arr[k];
                        }else if(sm!=arr[k]){
                            flag=false;
                            break;
                        }
                    }
                }
                if(flag){
                    m=Math.max(m,j-i+1);
                }
            }
        }
        return m;
    }
}

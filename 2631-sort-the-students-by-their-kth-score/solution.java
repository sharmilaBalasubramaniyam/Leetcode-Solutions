class Solution {
    public int[][] sortTheStudents(int[][] score, int k) {
        int n=score.length-1;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<score.length;j++){
                if(score[i][k]<score[j][k]){
                    int[] temp=score[i];
                    score[i]=score[j];
                    score[j]=temp;
                }
            }
        }
        return score;
    }
}

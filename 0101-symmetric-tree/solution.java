/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSymmetric(TreeNode root) {
        if(root==null) return true;
        return mirr(root.left,root.right);

    }
    public boolean mirr(TreeNode n,TreeNode n1){
        if(n==null && n1==null) return true;
        if(n==null || n1==null) return false;
        return (n.val==n1.val) && mirr(n.left,n1.right) && mirr(n.right,n1.left);
    }
}

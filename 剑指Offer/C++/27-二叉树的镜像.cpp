/*
输入一颗二叉树，输出它的镜像 
*/

/*
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};*/
class Solution {
public:
    void Mirror(TreeNode *pRoot) {
        if(pRoot == nullptr)
            return;
        if(pRoot->left == nullptr && pRoot->right == nullptr)
            return;
        
        TreeNode *pTemp = pRoot->left;
        pRoot->left = pRoot->right;
        pRoot->right = pTemp;
        
        if(pRoot->left)
            Mirror(pRoot->left);
        
        if(pRoot->right)
            Mirror(pRoot->right);
    }
};

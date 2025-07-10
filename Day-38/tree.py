class Treenode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def Preorder(root):
        if root == None:
            return
        
        

root=Treenode(1)
root.left=Treenode(2)
root.left.left=Treenode(4)
root.left.right=Treenode(5)
root.left.right.right=Treenode(11)
root.left.left.left=Treenode(9)
root.left.left.right=Treenode(10)
root.right=Treenode(3)
root.right.right=Treenode(6)
root.right.right.left=Treenode(7)
root.right.right.right=Treenode(8)

print(root.right.right.val)
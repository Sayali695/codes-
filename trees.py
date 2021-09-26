class node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    

    def PrintTree(self):
            if self.left:
               self.left.PrintTree()
            print(self.data)
            if self.right:
                self.right.PrintTree()
                

    def InsertData(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.InsertData(data)
            else:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.InsertData(data)
        else:
            self.data = data

    def InorderTraversal(self,root):
        if root != None:
            if root.left !=None:
                self.InorderTraversal(root.left)
            res.append(root.data)
            if root.right != None:
                self.InorderTraversal(root.right)
        return res
        
    def PreorderTraversal(self, root):
        res1 = []
        if root!=None:
            res1.append(root.data)
            res1 += self.PreorderTraversal(root.left)
            res1 += self.PreorderTraversal(root.right)

        return res1

    def PostorderTraversal(self,root):
        res2 = []
        if root !=None:
            res2+=self.PostorderTraversal(root.left)
            res2+=self.PostorderTraversal(root.right)
            res2.append(root.data)

        return res2

root = node(12)
root.InsertData(9)
root.InsertData(11)
root.InsertData(3)
root.InsertData(1)
root.InsertData(13)
root.InsertData(2)
root.InsertData(80)
res = []
print("Inorder Traversal->")
res = root.InorderTraversal(root)
print(res)
print("Preorder Traversal->")
res1 = []
res1 = root.PreorderTraversal(root)
print(res1)
print("Postorder Traversal->")
res2 = []
res2 = root.PostorderTraversal(root)
print(res2)
# root.PrintTree()
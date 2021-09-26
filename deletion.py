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

    def inorderpre(self,root):
        
        root = root.left
        while(root.right != None):
            root=root.right
        return root

    def inorderpost(self,root):
        
        root = root.right
        while(root.left != None):
            root=root.left
        return root
    

    def delete(self, root, data):
        if root == None:
            return None
        if root.left == None and root.right == None:
            del root
            return None
        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:

            pre = self.inorderpre(root)
            root.data = pre.data
            root.left = self.delete(root.left, pre.data)
        return root


root = node(12)
root.InsertData(9)
root.InsertData(11)
root.InsertData(3)
root.InsertData(1)
root.InsertData(13)
# root.InsertData(2)
root.InsertData(80)
root.PrintTree()
root.delete(root,1)
print()
root.PrintTree()
print(root.data)
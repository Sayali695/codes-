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
    def Search(self , root, data):
        
        # if self.data == data:
        #     print("Element Found")
        # elif data<self.data and self.left != None:
        #     self.left.Search(data)
        # elif data> self.data and self.right != None:
        #     self.right.Search(data)
        # else:
        #     print("Element not found")

       # OR

        if root is None or root.data == data:
            return data
        if data < root.data:
            return root.Search(root.left, data)
        return root.Search(root.right, data)


root = node(12)
root.InsertData(9)
root.InsertData(11)
root.InsertData(3)
root.InsertData(1)
root.InsertData(13)
root.InsertData(2)
root.InsertData(80)
print(root.Search(root, 7))
root.PrintTree()
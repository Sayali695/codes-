class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Operations:
    def insert(self,head,data):
        self.node = Node(data)
        if head == None:
            head = self.node
        else:
            temp = head
            while temp.next!=None:
                temp = temp.next
            temp.next = self.node
        return head 
        
    def print(self,head):
        temp = head
        while temp:
            print(temp.data,end = " ")
            temp = temp.next
    def reverse(self,head):
        pass



linked_list = Operations()
head = None
head = linked_list.insert(head, 11)
head = linked_list.insert(head, 25)
head = linked_list.insert(head, 38)
head = linked_list.insert(head, 46)
linked_list.print(head)
class BinaryTree():
    def __init__(self,value) -> None:
        self.value=value
        self.leftChild=None
        self.rightChild=None

    def insertLeft(self,value):
        if self.leftChild ==None:
            self.leftChild=BinaryTree(value)
        else:
            new_node=BinaryTree(value)
            new_node.leftChild=self.leftChild
            self.leftChild=new_node

    def insertRight(self,value):
        if self.rightChild == None:
            self.rightChild=BinaryTree(value)
        else:
            new_node=BinaryTree(value)
            new_node.rightChild=self.rightChild
            self.rightChild=new_node

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.value)
        if self.rightChild:
            self.rightChild.inorder()
    
    def preorder(self):
        print(self.value)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.value)

a_node = BinaryTree('a')
a_node.insertLeft('b')
a_node.insertRight('c')

b_node = a_node.leftChild
b_node.insertRight('d')

c_node = a_node.rightChild
c_node.insertLeft('e')
c_node.insertRight('f')

d_node = b_node.rightChild
e_node = c_node.leftChild
f_node = c_node.rightChild

# print(a_node.value) # a
# print(b_node.value) # b
# print(c_node.value) # c
# print(d_node.value) # d
# print(e_node.value) # e
# print(f_node.value) # f

a_node.inorder()

print("*"*20)

a_node.preorder()

print("$"*20)

a_node.postorder()
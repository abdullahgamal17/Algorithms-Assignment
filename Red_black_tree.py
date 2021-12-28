class node():
    def __init__(self,val=0,left=None,right=None,color ="red"):
        self.key = val
        self.left = left
        self.right = right
        self.color = color
        self.parent = None
        self.left_size = 0
        self.right_size = 0
    

class RBT():
    def __init__(self):
        self.root = None
        self.size = 0
        self.num_black_nodes = 0
        self.leftleft = False
        self.leftright = False
        self.rightright = False
        self.rightleft = False
    
    #flags
    
    
    def rotate_left(self,node):
        x = node.right
        T3 = x.left
        x.left = node
        node.right = T3
        node.parent = x
        
        
        
        if T3!=None:
            T3.parent = node
            node.right_size = node.right_size + T3.right_size + 1
        else:
            node.right_size = 0
        x.left_size = node.left_size + node.right_size + 1
            
        return x
    
    def rotate_right(self,node):
        x = node.left
        T2 = x.right
        x.right = node
        node.left = T2
        node.parent = x
        
        
        if T2!=None:
            T2.parent = node
            node.left_size = T2.right_size + T2.left_size + 1
        else:
            node.left_size = 0
        x.right_size = node.left_size + node.right_size + 1
        
        return x
    
    def helper(self,root,data):
        f = False
        
        if root == None:
            return node(data)
        elif(data < root.key):
            root.left = self.helper(root.left,data)
            root.left_size = root.left_size + 1
            root.left.parent = root
            if root != self.root:
                if root.color =="red" and root.left.color =="red":
                    f = True
        else:
            root.right = self.helper(root.right,data)
            root.right_size = root.right_size + 1
            root.right.parent = root
            if root != self.root:
                if root.color =="red" and root.right.color =="red":
                    f = True
        
        
            
            
        if self.leftleft:
            root = self.rotate_left(root)
            root.color = "black"
            root.left.color = "red"
            self.leftleft = False
        
        elif self.rightright:
            root = self.rotate_right(root)
            root.color = "black"
            root.right.color = "red"
            self.rightright = False
        
        elif self.rightleft:
            root = self.rotate_right(root.right)
            root.right.parent = root
            root = self.rotate_left(root)
            root.color = "black"
            root.left.color = "red"
            self.rightleft = False
        
        elif self.leftright:
            root.left = self.rotate_left(root.left)
            root.left.parent = root
            root = self.rotate_right(root)
            root.color = "black"
            root.right.color = "red"
            self.leftright = False
        
        
        if f:
            if root.parent.right == root:
                if root.parent.left == None or root.parent.left.color =="black":
                    if root.left != None and root.left.color =="red":
                        self.rightleft = True
                    elif root.right!=None and root.right.color =="red":
                        self.leftleft = True
                else:
                    root.parent.left.color = "black"
                    root.color = "black"
                    if root.parent != self.root:
                        root.parent.color = "red"
            else:
                if root.parent.right == None or root.parent.right.color =="black":
                    if root.left != None and root.left.color =="red":
                        self.rightright = True
                    elif root.right!=None and root.right.color =="red":
                        self.leftright = True
                else:
                    root.parent.right.color = "black"
                    root.color = "black"
                    if root.parent != self.root:
                        root.parent.color = "red"
            f = False
    
        return root
    
    def insert(self,data):
        
        if self.root == None:
            self.root=node(data)
            self.root.color = "black"
        else:
            self.root = self.helper(self.root,data)
        
        
    def search(self,data):
        
        if self.root != None :
            if data > self.root.key:
                newtree = RBT()
                if self.root.right == None:
                    return -1
                newtree.root = node(self.root.right.key,right = self.root.right.right,left = self.root.right.left,color = self.root.right.color)
                return self.root.left_size + 1 + newtree.search(data) 
            elif data < self.root.key:
                newtree = RBT()
                if self.root.left == None :
                    return -1
                newtree.root = node(self.root.left.key,right = self.root.left.right,left = self.root.left.left,color = self.root.left.color)
                return newtree.search(data)
            else:
                return self.root.left_size 
        else:
            return -1000

def problem9(Q):
    output = []
    tree = RBT()
    for i in range(Q):
        inp = input().split()
        command = int(inp[0])
        value = int(inp[1])
        if(command == 1):
            tree.insert(value)
        elif(command == 2):
            output.append(tree.search(value)+1)
    
    for res in output:
        if res > 0:
            print(res ,end=" ")
        else:
            print(-1,end=" ")
        

problem9(10)        
        
import numpy as np 

#Implement class node to be used in the skip list
class node():
    def __init__(self,key):
        #value
        self.key = key
        self.right = None
        self.left = None
        self.down = None
        self.up = None
        self.index = -1

#implement the skip list data structure        
class skip_list():
    
    def __init__(self):
        #Constants
        self.NEG_INF = -np.inf
        self.POS_INF = np.inf
        
        #Extremes
        self.head = node(self.NEG_INF)
        self.tail = node(self.POS_INF)
        self.head.right = self.tail
        self.tail.left = self.head
        
        #Levels
        self.level = 0 #height of the skip list
    
    def search(self,key):
        n = self.head
        while(n.down != None):
            n = n.down
            while(key >= n.right.key):
                n = n.right
        return n
    
    def search_steps(self,key):
        n = self.head
        steps = 0
        found = 0
        while(n.down != None):
            n = n.down
            steps+=1
            while(key >= n.right.key):
                n = n.right
                steps+=1
        
        if n.key == key:
            found = 1
        else:
            found = 0
        
        if found == 1:
            print(steps)
        else:
            print(-1)
        return n
    
    def add_empty_level(self):
        new_head_node = node(self.NEG_INF)
        new_tail_node = node(self.POS_INF)
        
        new_head_node.right = new_tail_node
        new_head_node.down = self.head
        new_tail_node.left = new_head_node
        new_tail_node.down = self.tail
        
        self.head.up = new_head_node
        self.tail.up = new_tail_node
        
        self.head = new_head_node
        self.tail = new_tail_node
        
    def can_increase_level(self,level):
        if (level >= self.level):
            self.level += 1
            self.add_empty_level()
    
    def set_before_and_after_references(self,q,newnode):
        newnode.right = q.right
        newnode.left = q
        q.right.left = newnode
        q.right = newnode
        
    def set_above_and_below_references(self,pos,key,newnode,nodebeforenewnode):
        if nodebeforenewnode != None:
            while True:
                if nodebeforenewnode.right.key != key:
                    nodebeforenewnode = nodebeforenewnode.right
                else:
                    break
        
            newnode.down = nodebeforenewnode.right
            nodebeforenewnode.right.up = newnode
        
        if pos != None:
            if pos.right.key == key:
                newnode.up = pos.right
                      
    def insert_after_above(self,pos,q,key):
        new_node = node(key)
        node_before_new_node = pos.down.down
        self.set_before_and_after_references(q,new_node)
        self.set_above_and_below_references(pos,key,new_node,node_before_new_node)
        
        return new_node
            
    def insert_node(self,key):
        # Create a new node
        iters = 0
        pos = self.search(key)
        levels = 0
        number_of_heads = 0
        
        if pos.key == key:
            return pos
        
        
        
        while(not iters or np.random.choice([0,1],p=[0.5,0.5])):
            
            self.can_increase_level(levels) 
            q = pos
            while(pos.up == None):
                pos = pos.left
            pos = pos.up
            q = self.insert_after_above(pos,q,key)
            number_of_heads += 1
            levels += 1
            iters += 1
            
        return q
    
    def get_layers(self):
        return self.level
    
    def print_level(self,level):
        empty_string = ""
        text = (f"\nLevel: {level} \n")
        empty_string += text
        start = self.head
        highestlevel = start
        number_of_levels = self.level
        downs = number_of_levels - level
        if downs < 0:
            print("Level does not exist")
            return None
        for i in range(downs):
            highestlevel = highestlevel.down
        while(highestlevel != None):
            text = (f"{highestlevel.key} ")
            empty_string += text
            if start.right != None:
                    empty_string += " : "
            highestlevel = highestlevel.right
        print(empty_string)
    
    def remove_references_to_node(self,node_to_delete):
        after_node_to_delete = node_to_delete.right
        before_node_to_delete = node_to_delete.left
        
        before_node_to_delete.right = after_node_to_delete
        after_node_to_delete.left = before_node_to_delete
        
    def delete(self,key):
        node_to_delete = self.search(key)
        if node_to_delete.key != key:
            return None
        
        self.remove_references_to_node(node_to_delete)
        
        while node_to_delete != None:
            self.remove_references_to_node(node_to_delete)
            
            if node_to_delete.up != None:
                node_to_delete = node_to_delete.up
            else:
                break
            
    def print_list(self):
        empty_string = ""
        start = self.head
        highestlevel = start
        level = self.level
        
        while highestlevel != None:
            text = (f"\nLevel: {level} \n")
            empty_string += text
            while start != None:
                empty_string += (f"{start.key} ")
                if start.right != None:
                    empty_string += " : "
                start = start.right
            highestlevel = highestlevel.down
            start = highestlevel
            level -= 1
        print(empty_string)
            
                
                    
        
         
         
            
        
                 
        
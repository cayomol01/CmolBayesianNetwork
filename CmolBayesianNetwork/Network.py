from Node import Node
class Network():
    def __init__(self, nodes) -> None:
        self.nodes = [Node(node) for node in nodes]
        
    def addNode(self, name,  parents = None, next = None):
        names = [i.name for i in self.nodes]
        for i in self.nodes:
            if name == i.name:
                print("Node already exists")
                return
            
        for i in parents:
            if i not in names:
                print("A parent does not exist")
                return
        
        
            
        for i in next:
            if i not in names:
                print("Next node does not exist")
                return
            
        self.nodes.append(Node(name,parents,next))
            
        
    def addProbs(self, name, dic):
        pass
        
            

            
        
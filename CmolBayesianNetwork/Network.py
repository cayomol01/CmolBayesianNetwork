from Node import Node
class Network():
    def __init__(self, nodes) -> None:
        self.nodes = [Node(node) for node in nodes]
        self.names =  [i.name for i in self.nodes]
        
    def addNode(self, name,  parents = None, next = None):
        for i in self.nodes:
            if name == i.name:
                print("Node already exists")
                return
            
        for i in parents:
            if i not in self.names:
                print("A parent does not exist")
                return
        
        
            
        for i in next:
            if i not in self.names:
                print("Next node does not exist")
                return
            
        self.nodes.append(Node(name,parents,next))
        self.names.append(name)
            
        
    def addProbs(self, name, dic):
        idx = self.names.index(name)
        nodo = self.nodes[idx]
        #Se agregan las probabilidades en forma {"A|B": 0.01}
        nodo.addProbs(dic)
        
    def formaCompacta(self):
        res= ""
        for i in self.nodes:
            if len(i.parents)==0:
                res+=f'P(%s)'%i.name
            else:
                res+= f"P(%s|%s)" %(i.name,''.join(i.parents))
        print(res)
                
    def addParents(self, name, parents):
        idx = self.names.index(name)
        nodo = self.nodes[idx]
        
        nodo.setParents(parents)
        
    
    
        
        
        
        
        
            

            
        
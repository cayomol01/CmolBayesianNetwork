class Node():
    def __init__(self, name, parents = None, next = None) -> None:
        self.name = name
        self.probs = {}
        self.parents = parents or []
        self.next = next or []
        
    def setParents(self, parent):
        self.parents = parent

    def addNext(self, value):
        self.next.append(value)
        
    def addProbs(self, dic):
        self.probs.update(dic)
        
    def checkCompletion(self):
        if len(self.parents) == 0:
            return self.probs.get(self.name)
        else:
            return len(self.probs)>=2**len(self.parents)


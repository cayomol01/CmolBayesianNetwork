class Node():
    def __init__(self, name, parents = None, next = None):
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
        return len(self.probs)>=2**len(self.parents) if self.parents else self.probs.get(self.name)

    def getProbs(self, value):
        return self.probs.get(value)

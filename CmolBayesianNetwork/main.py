from Network import Network


nodos = ['A', 'B', 'C', 'E', 'F', 'G', 'H']
bayes = Network(nodos)
bayes.addParents('C', ['A', 'B'])
bayes.addParents('E', ['C'])
bayes.addParents('F', ['C'])
bayes.addParents('G', ['F'])
bayes.addParents('H', ['F', 'E', 'G'])
print(bayes.formaCompacta())

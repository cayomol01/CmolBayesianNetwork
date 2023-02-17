from Network import Network


nodos = ['A', 'B', 'C', 'E', 'F']
bayes = Network(nodos)
bayes.addParents('C', ['A', 'B'])
bayes.addParents('E', ['C'])
bayes.addParents('F', ['C'])
bayes.formaCompacta()
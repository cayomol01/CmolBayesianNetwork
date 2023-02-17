from Network import Network


nodos = ['A', 'B', 'C', 'D', 'E']
bayes = Network(nodos)
bayes.addParents('C', ['A', 'B'])
bayes.addParents('D', ['C'])
bayes.addParents('E', ['C'])

print(bayes.formaCompacta())


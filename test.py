
from prepare import readData,getTitles
from DecisionTree import DecisionTree

tree = DecisionTree(readData(),getTitles())
tree.generate()
tree.print()

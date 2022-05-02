from utils import *
from tree import Node
import copy

class DecisionTree():
    def __init__(self,D,titles):
        self.D = D
        self.tempD = []
        self.splitedD= []
        self.children = []
        self.tags = []
        self.index = -1
        self.titles = titles

    def scan(self,col):
        self.tempD = []
        types = []
        typenums = []
        for row in self.D:
            if row[col] not in types:
                types.append(row[col])
                typenums.append(1)
            else:
                typenums[types.index(row[col])] = typenums[types.index(row[col])] + 1

        for i in types:
            temp = []
            for row in self.D:
                if row[col] == i:
                    temp.append(row)
            self.tempD.append(temp)

        return types,typenums

    def split(self,nameindex,types):
        self.tempD = self.D
        for j in types:
            data = []
            for i in range(len(self.D)):
                if self.D[i][nameindex] == j:
                    row1 = self.D[i]
                    row1.pop(nameindex)
                    data.append(row1)
            self.splitedD.append(data)



    def generate(self):
        com_row = self.D[0]
        for i in range(len(self.D)):
            if (self.D[i][-1] == com_row[-1]):
                if (i == len(self.D) - 1):
                    #print('done')
                    return 1
            else:
                break

        nameindex = []
        gains = []
        for j in range(len(self.D[0])-1):
            nameindex.append(j)
            types,typenums=self.scan(j)
            rootEnt = getRootEnt(self.D)
            ents = []
            for datas in self.tempD:
                ents.append(getRootEnt(datas))
            gain = getGain(rootEnt,typenums,ents)
            gains.append(gain)

        max_index = -1
        max = -9999
        for i in range(len(gains)):
            if gains[i] > max:
                max_index = i
                max = gains[i]

        types,typenums = self.scan(max_index)
        self.split(max_index,types)
        self.index = max_index
        titles = copy.deepcopy(self.titles)
        titles.pop(self.index)
        for i in range(len(self.splitedD)):
            self.tags.append(types[i])
            self.children.append(DecisionTree(self.splitedD[i],titles))
            self.children[i].generate()

    def print(self):
        if self.titles[self.index] == 'result':
            print(self.D[0][-1])
        else:
            print(self.titles[self.index])
        if len(self.children):
            for i in range(len(self.children)):
                child = self.children[i]
                child.print()


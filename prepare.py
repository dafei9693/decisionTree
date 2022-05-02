

def readData():
    with open('DataSet','r') as f:
        text = f.read()
        list = text.split()
        dataset = []
        row = []
        for i in range(1,len(list)+1):
            row.append(list[i-1])
            if i%5 == 0 and i!=0:
                dataset.append(row)
                row = []

    return dataset

def getTitles():
    with open('tetles','r') as f:
        text = f.read()
        titles = text.split(' ')
        return titles


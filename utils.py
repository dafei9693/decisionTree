import math



def getEntropy(totle,opt):
    if opt==0:
        return -math.log((totle-opt)/totle,2)*(totle-opt)/totle
    elif opt==totle:
        return -math.log(opt/totle,2)*opt/totle
    return -math.log(opt/totle,2)*opt/totle-math.log((totle-opt)/totle,2)*(totle-opt)/totle



def getGain(ent,types,ents):
    totle = 0
    for i in types:
        totle = totle+i
    for i in range(len(types)):
        ent = ent - types[i]/totle*ents[i]
    return ent

def getRootEnt(data):
    opt = 0
    for row in data:
        if row[-1] == 'yes':
            opt = opt + 1

    return getEntropy(len(data),opt)




class Node():
    def __init__(self,val,children,tags):
        self.val = val
        self.children = children
        self.tags = tags


    def print(self):
        print(self.val)
        for tag in self.tags:
            print(tag)
        if self.children:
            for child in self.children:
                self.print()

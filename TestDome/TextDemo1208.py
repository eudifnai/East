
class TestDome1208(object):
    items = ['item1', 'item2', 'item3', 'item1']
    data = [[1, 2, 3], ['a', 'b', 'c'], 'x', 'y']
    #01
    def fun(self):
        for i in range(len(self.items)):
            print(i+1, ':', self.items[i])

    #02
    def fun1(self):
        for i, item in enumerate(self.items):
            print(i, ':', item)

    #03
    def strconnect(self,index):
        s = ''
        num = 0
        for i in range(len(self.data)):
            if i == index:
                d = self.data[i]
                for j in range(len(d)):
                    if isinstance(d[j], str):
                        s += str(ord(d[j]))
                    elif not isinstance(d[j], str):
                        num += d[j]
        if num == 0:
            return s
        else:
            return num







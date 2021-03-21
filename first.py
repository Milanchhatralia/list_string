

class ListString():  
    strList = []
      
    def getMostRepeatedK(self, k):
        d = dict() # {item: occurence,}
        for item in self.strList:
            if item not in d:
                d[item] = 1
            else:
                d[item] = d[item]+1
                
        
        if(len(d) < k):
            return ''
        
        # print(d)
        
        occ = dict()
        for num, freq in d.items():
            if(freq not in occ):
                occ[freq] = [num]
            else:
                temp = occ[freq]
                temp.append(num)
                occ[freq] = temp
        
        print(occ)
        
        for num, a in occ.items():
            print(a)
            if(k==0):
                print("returning :"+a)
                return a
            k = k - 1
            # print(k)

    def insertIntoList(self, item):
        self.strList.append(item)
        print('Added: '+item)



if __name__ == '__main__':
    
    fruit = ListString()
    fruit.insertIntoList('apple')
    fruit.insertIntoList('apple')
    fruit.insertIntoList('orange')
    print(fruit.getMostRepeatedK(2))
    
    fruit.insertIntoList('mango')
    fruit.insertIntoList('mango')
    fruit.insertIntoList('mango')
    print(fruit.getMostRepeatedK(3))
    print(fruit.getMostRepeatedK(1))
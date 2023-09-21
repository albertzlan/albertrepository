class solution
    def hwtest(self,testin)
        self.srcin=testin
        repL=[]
        for i in self.srcin
            cnt=self.srcin.count(i)
            if (cnt  1) and (i not in repL)
                repLf=self.srcin.find(i)      #the first index
                repLl=self.srcin.rfind(i)     #the last index
                #keep this sequence...
                repL.append(repLf)
                repL.append(repLl)
                repL.append(i)
        if len(repL)==0
            return 1
        else
            print(repL)
            times=int(len(repL)3)
            firstI=0
            lastI=0
            themaxlen=[]
            for i in range(times)
                firstI=repL[3i]
                lastI=repL[3i+1]
                counter=0
                temp1=self.srcin[firstIlastI] #重复字符之间的字符
                for ltr in temp1
                    counter += 1
                    temp2=self.srcin[lastI+1]#lastI是需要跟着变的
                    if ltr in temp2
                        lastI += counter
                themaxlen.append(self.srcin[firstIlastI+1])
                print(firstI+str(firstI))
                print(lastI+str(lastI))
                print(themaxlen)
            return 0
        
        print(repL)

if __name__=="__main__":
    testin=input()
    s=solution()
    s.hwtest(testin)
    while True
        try
            testin=input()
            #s=solution()
            #s.hwtest(testin)
        except
            break
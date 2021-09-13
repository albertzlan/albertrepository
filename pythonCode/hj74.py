def hj74(testsr):
    srcin=str(testsr)
    dstout=[]
    
    
    
    if "\"" in srcin:
        firstsplit=srcin.split("\"")
        #print(firstsplit)
        for i in range(len(firstsplit)):
            if firstsplit[i]=="" or firstsplit[i]==" ":
                firstsplit=firstsplit[:i]+firstsplit[i+1:]
        
        secondsplit=""
        for i in firstsplit:
            secondsplit=secondsplit+i
        #print(secondsplit)
        dstout=secondsplit.split()
    else:
        dstout=srcin.split()
    return dstout
if __name__=="__main__":
    while True:
        try:
            testin=input()
            testout=hj74(testin)
            print(len(testout))
            for i in testout:
                print(i)
        except:
            break

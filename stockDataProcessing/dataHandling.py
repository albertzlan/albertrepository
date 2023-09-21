
import re
from numpy import *
import matplotlib.pyplot as plt

def dataPreprocessing():
    '''
    date,OpenPr,ClosePr,HighPr,LowPr,Volume,Turnover,Change,ChgVal,ExchgRate
    2011-01-25
    开盘 6.88，收盘6.29，最高6.88，最低6.18，
    成交量20944，成交额94150184.00，
    涨跌幅-14.65，涨跌额-1.08，换手率23.48

    '''
    #open file handler
    srcfh=open('preDailyKlines000069','r',encoding="UTF-8")
    dstfh=open('processedDailyPrice000069','w',encoding="UTF-8")
    tmp=str(srcfh.readlines())
    #print(tmp)

    #changing matching mode from greedy to lazy: '.*?' OR '.+?' 
    pt01=re.compile('\"([0-9\-]{8}).+?\"') 

    ret=re.findall(r'"([0-9]{4,}-[0-9]{2,}-[0-9]{2,},[0-9,\-\.]{10,})"',tmp)
    #print(len(ret))

    #将处理后的数据写入dstfh文件中
    #dstfh.write("date,OpenPr,ClosePr,HighPr,LowPr,Volume,Turnover,Change,ChgVal,ExchgRate"+"\r")
    closePr=[]#Close Price each day.
    for i in ret[5700:]:#后面调试用，不需太多数据
    #for i in ret:
        #print(i)
        #dstfh.write(str(i)+"\r")
        sp=i.split(",")
        #print(sp)
        closePr.append(float(sp[2]))

    #close file handler
    srcfh.close()
    dstfh.close()
    
    print('Days:'+str(len(closePr)))
    return closePr
    
def tradingStrategy_MACrossing(closePrice):
    '''
    基于简单MA双线交叉de交易策略
    资金管理采用全买全卖策略；
    '''
        #tradeStrategy:基于简单MA双线交叉de交易策略,且资金管理采用全买全卖策略；
    MA05=5
    MA10=10
    floatMA05=[]
    floatMA10=[]
    tmpclosePr=closePrice[:]#深拷贝
    #calculate MA05,MA10
    for inttmp in range(MA10,len(tmpclosePr)+1):
        floatMA05.append(mean(tmpclosePr[inttmp-MA05:inttmp]))
        floatMA10.append(mean(tmpclosePr[inttmp-MA10:inttmp]))
##        print("========:"+str(inttmp))
##        print(tmpclosePr[inttmp-MA05:inttmp])
##        print(floatMA05)
##        print(tmpclosePr[inttmp-MA10:inttmp])
##        print(floatMA10)

    # tradingStrategy: sell or buy
    tradingStrategy=[]
    cashFlag=100000 #RMB:Yuan
    positionFlag=0
    commissionFlag=0
    plt_Cash=[100000]
    plt_cashIndex=[0]
    plt_Position=[0]
    plt_positionIndex=[0]
    plt_commission=[0]
    for inttmp in range(len(floatMA05)):
        # to buy: MA05上穿MA10，且有现金，则当天收盘价买入
        if (floatMA05[inttmp]-floatMA10[inttmp])>=0.00001 and cashFlag>0:
            tradingStrategy.append('BUY')
            tradingStrategy.append(inttmp)
            positionFlag=int(float(cashFlag)/float(tmpclosePr[inttmp]))
            #计算扣除佣金额度后再将cashFlag归零
            commissionFlag=int(float(cashFlag)*0.0002)
            cashFlag=0
            #打印过程中的筹码情况
            print(str(inttmp)+"    BUY__positionFlag:"+str(positionFlag)+";    BUY__cashFlag:"+str(cashFlag))
            plt_Position.append(positionFlag)
            plt_positionIndex.append(inttmp)
            
        # to sell: MA10下穿MA05，且有筹码，则当天收盘价卖出
        if (floatMA05[inttmp]-floatMA10[inttmp])<=0.00001 and positionFlag>0:
            tradingStrategy.append('SELL')
            tradingStrategy.append(inttmp)
            cashFlag=int(positionFlag*tmpclosePr[inttmp])
            positionFlag=0
            #打印过程中的现金情况
            print(str(inttmp)+"    SELL__positionFlag:"+str(positionFlag)+";    SELL__cashFlag:"+str(cashFlag))
            plt_Cash.append(cashFlag)
            plt_cashIndex.append(inttmp)
            ##扣除佣金
            commissionFlag=int(float(cashFlag)*0.0002)+commissionFlag#一轮买卖此处一起扣除
            plt_commission.append(commissionFlag)
            cashFlag=cashFlag-commissionFlag
             
    print("FINAL_cashFlag:"+str(cashFlag))
    print("FINAL_positionFlag:"+str(positionFlag))
    #print(tradingStrategy)
    
    #画出：收盘价 MA5 MA10 三条曲线
    plt_closePr=closePrice
    plt_floatMA05=[6]*(MA10-1)+floatMA05
    plt_floatMA10=[6]*(MA10-1)+floatMA10
    fig,ax=plt.subplots(4)
    ax[0].plot(plt_closePr,label='plt_closePr',marker='.')
    #ax[0].plot(plt_floatMA05,label='plt_floatMA05',marker='+')
    #ax[0].plot(plt_floatMA10,label='plt_floatMA10',marker='+')
    ax[0].legend()#显示label
    ax[1].plot(plt_cashIndex,plt_Cash,label='plt_Cash',marker='.')
    ax[1].legend()#显示label
    ax[2].plot(plt_positionIndex,plt_Position,label='plt_Position',marker='.')
    ax[2].legend()#显示label
    ax[3].plot(plt_cashIndex,plt_commission,label='plt_commission:'+str(sum(plt_commission)),marker='.')
    ax[3].legend()#显示label
    #plt.xticks([])
    plt.show()
##    fig.suptitle('closePr.coral    floatMA05+blue    floatMA10+green')
##    plt.plot(plt_closePr,marker='.',color='coral')
##    plt.plot(plt_floatMA05,marker='+',color='blue')
##    plt.plot(plt_floatMA10,marker='+',color='green')


def tradingStrategy_GodInsight():
    '''#tradingStrategy_GodInsight:上帝视角：相比上一天涨则当天收盘价买，降则当天收盘价卖；且资金管理采用全买全卖策略。
    '''
    print('tradingStrategy_GodInsight...')
    
    
   
if __name__=="__main__":
    price=dataPreprocessing()
    tradingStrategy_MACrossing(price)
    

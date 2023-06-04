import random

def randomList(n):
    iList = []
    for i in range(n):
        iList.append(random.randrange(1000)) # append()函数用于产生随机数存入iList列表中
    return iList
iList1=randomList(20)
def bubbleSort(iList):
    """冒泡排序"""
    if len(iList1) <=1:
        return iList1
    for i in range(1,len(iList1)):
        for j in range(0,len(iList1)-i):
            if iList[j] >= iList[j+1]:

                iList1[j], iList1[j+1] = iList1[j+1], iList1[j]
        print("第%d轮排序结果为：" %i, end=" ")
        print(iList1)
    return iList
if __name__ == "__main__":
    print(iList1)
    print("冒泡排序结果：",bubbleSort(iList1))

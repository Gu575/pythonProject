#打印一条横线
def line(rows):
    for i in range(rows):
        print("-"*30)

a = input("input:")
print(line(int(a)))

#列表求和：
def sum(list):
    s = 0
    for x in list:
        s += x
        return s

#求三个数的平均值
def ave(list):
    avg = 0
    avg =sum(list)/(len(list))
    return avg

list =[1,3,6]
print(ave(list))
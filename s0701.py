#lamda判断一个数是奇数还是偶数
a=lambda x:"偶数" if x%2==0 else "奇数"
print(a(5))
arr=[1,3,5,7,9]
arr=list(map(lambda x:x**2,arr))
print(arr)
lst=[]
for i in range(100):
    lst.append("data"+str(i))
print(lst)
#列表推导式
print(["data{}".format(i) for i in range(0,100,2)])
x=list("data"+str(y) for y in range(100) if y%2!=0)
print(x)
#[“data0”,“gy1”,“data2”,“gy3”,…,“data98”,“gy99”]
print(["data{}".format(i) if i%2==0 else "gy{}".format(i) for i in range(100)]
print(["gy{}".format(i) for i in range(1, 100, 2)])

costprice=int(input("Enter the cp: "))
sellingprice=int(input("Enter the sp: "))
if(sellingprice>costprice):
    print("profit")
    pt=sellingprice-costprice
    print(pt)
else:
    print("loss")
    ls=sellingprice-costprice
    print(ls)
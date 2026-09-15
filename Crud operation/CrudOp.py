product=[]
def add():
    pid=int(input("Enter PID  "))
    pname=input("Enter Product name  ")
    price=int(input("Enter Product Price "))

    d1={"PID":pid,"PName":pname,"Price":price}
    product.append(d1)
def display():
    print("===================================")
    print("Product ID Product Name Product  Price")
    print("===================================")
    for p1 in product:
        print(p1["PID"],"       ",p1["PName"],"       ",p1["Price"])
def search():
    pid=int(input("Enter PID"))
    found=0
    for p1 in product:
        if(p1["PID"]==pid):
            found=1
            break
    if(found==1):
        print("Product is found")
        print("===================================")
        print("Product ID Product Name Product  Price")
        print("===================================")
        print(p1["PID"],"       ",p1["PName"],"       ",p1["Price"])
    else:
        print("Not found")
def updateName():
    pid=int(input("Enter PID which name u want to change "))
    found=0
    for p1 in product:
        if(p1["PID"]==pid):
            found=1
            break
    if(found==1):
        print("Product is found")
        pname=input("Enter New  Product name")
        p1["PName"]=pname
        print("===================================")
        print("Product ID Product Name Product  Price")
        print("===================================")
        print(p1["PID"],"       ",p1["PName"],"       ",p1["Price"])
    else:
        print("Not found")
def deletebyPID():
    pid=int(input("Enter PID which name u want to delete "))
    found = 0

    for p1 in product:
        if p1["PID"] == pid:
            product.remove(p1)
            found = 1
            print("Product is deleted successfully")
            break
    if found == 0:
        print("Not found")
def sortByPrice():
    if not product:
        print("No products available to sort.")
        return
    product.sort(key=lambda x: x["Price"])
    print("Products sorted by price successfully!")
    display()  






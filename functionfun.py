# function name: "getmoney"
# behavior: prints the string "cash"
def getmoney():
    print("cash")

# function name: "gettenmoney"
# behavior: calls getmoney 10 times
def gettenmoney():
    i = 0
    while(i < 10):
        getmoney()
        i+=1

# run gettenmoney
gettenmoney()

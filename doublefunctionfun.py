# function name: "getmoney"
# behavior: returns the string "cash"
def getmoney():
    return "cash"

def create_message(input_number, input_string):
    the_message = ''
    the_message += str(input_number)
    the_message += '. '
    the_message += input_string
    the_message += ' '
    return the_message

# function name: "gettenmoney"
# behavior: calls getmoney 10 times
def gettenmoney():
    i = 1
    while(i <= 10):
        print(create_message(i, getmoney()))
        i+=1

# run gettenmoney
gettenmoney()

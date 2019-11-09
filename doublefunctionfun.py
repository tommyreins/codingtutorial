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
        cash_string = getmoney()
        count_of_cash = create_message(i, cash_string)
        print(count_of_cash)
        i+=1

# run gettenmoney
gettenmoney()

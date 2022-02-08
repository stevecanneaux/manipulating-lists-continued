numList = list();


while(True):
    inputStr = input("enter a number: ")
    if(inputStr == "done") :
        break
    value = float(inputStr)
    numList.append(value)

average = sum(numList) / len(numList)
print("Average is: ", average)

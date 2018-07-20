
#excercise 1
total = 0
for num in range(101):
    print(num)

#excercise 2
endPoint = int(input("enter a number."))
num = 0

total1 = 0
while (num < endpoint):
    num += 1
    print(num)
    total1 += num
    print(total1)

#excercise 3

input = input("press q to quit")

while(input1 != "q"):
    input1 = input("press q to tquit")



#excercise 4

input1 = input("press q to quit")
iQuit = input("Enter a quit word")
while (input != iQuit):
    input1 = input("press q to quit")


# excercise 5
def forLoopFunction():
    smallArray = []
    while True:
        userInput = input("whatever?: or 'q' to quit")
    if userInput =="q":
        for a in smallArray:
            print(a)
        break

    else: smallArray.append(userInput)

forLoopFunction()
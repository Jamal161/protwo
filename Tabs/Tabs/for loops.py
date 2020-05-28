# for i in range(1,10):
#     print("i is {} now".format(i))

# number = "1,12,14,52,65,78,452,145,124,75,1545,925"
# for i in range(1, len(number)):
#     print(number[i])

# number = "1,12,14,52,65,78,452,145,124,75,1545,925"
# for i in range(1, len(number)):
#     if number[i] in '0123456789':
#         print(number[i])


for i in range(1,13):
    for j in range(1,13):
        print("{1} times {0} is {2}".format(i,j,i**j), end='\t')
    print("====================")
number = input("enter blocks:")
number = int(number)

i = 0
list_of_blocks = []
while i<number :
    hight_of_block = input("high of block:")
    hight_of_block = int(hight_of_block)
    list_of_blocks+=[hight_of_block]
    i+=1
print(list_of_blocks)


j = 0
counter = 1
max_hight = list_of_blocks[0]
if len(list_of_blocks)==0 :
    print(0)

while j<(len(list_of_blocks)-1):

    if list_of_blocks[j]<list_of_blocks[j+1] and list_of_blocks[j+1]>max_hight:
        counter+=1
        max_hight = list_of_blocks[j+1]

    j+=1

print (counter)


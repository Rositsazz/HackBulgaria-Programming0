string = input("Please, enter text: ")
text = string

vowels = "aeiouyAEIOUY"
counter = 0 

for ch in string :
    
    if ch in vowels :
        counter+=1
        
print("\"" + text + "\"" + " - " + str(counter))

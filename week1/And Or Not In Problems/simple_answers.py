string = input("Hello, stranger! ")
search1 = "hello"
search2 = "Hello"
search3 = "how are you?"
search4 = "feelings"
search5 = "age"

if search1 or search2 in string :
    print("Hello there, good stranger!")

elif search3 in string :
    print("I am fine, thanks. How are you?")

elif search4 in string :
    print("I am a machine. I have no feelings")

elif search5 in string :
    print("I have no age. Only current timestamp")

else :
    print("Not such word")

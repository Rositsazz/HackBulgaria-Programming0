def str_reverse(string) :
    new_string = string[::-1]
    return new_string

def join(delimiter, items) :
    new_string = ""
    for item in items:
        new_string += item+delimiter
    new_string = new_string[:len(new_string)]
    return new_string

def startswith(search,string) :
    new_string = string[:len(search)]
    if new_string==search:
        return True
    return False

def endswith(search, string) :
    new_string = string[len(string)-len(search):]
    if new_string==search :
          return True
    return False

def endswith(search, string) :
    search = str_reverse(search)
    string = str_reverse(string)
    return startswith(search, string)

def trim(string) :
    str1 = string.lstrip()
    str1 = str_reverse(str1)
    str1 = str1.lstrip()
    str1 = str_reverse(str1)
    return str1

def trim(string) :
    for character in string :
        if startswith(" ", string):
            string = string[1:]
        elif endswith(" ", string):
            string = string[:len(string)-1]
    return string

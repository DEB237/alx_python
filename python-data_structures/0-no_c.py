def no_c(my_string):
    new_string = list(my_string)
    for char in my_string:
        if char.lower() == 'c':
            new_string.remove(char)
    return ''.join(new_string) 

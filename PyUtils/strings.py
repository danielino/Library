
def clean_new_line(string):
    char_to_remove = ['\n','\r']
    tmp = string
    for i in char_to_remove:
        tmp = tmp.replace(i, '')
        
    return tmp
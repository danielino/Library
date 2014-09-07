

def file_exists(fileName):
    try:
        open(fileName).close()
        return True
    except: 
        return False


def open_file(fileName, mode = 'r'):
    try:
        return open(fileName, mode)
    except:
        return False


def write_file(fileName, text):
    try:
        fp = open_file(fileName,'a+')
        fp.write(text)
        fp.close()
        return True
    except Exception as error:
        return error
    
    
def read_file(filePointer):
    return filePointer.readlines()

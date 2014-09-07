from time import strftime
from PyUtils import strings




def get_date_for_log():
    ''' return format: yymmddHHMM '''
    return strftime("%y%m%d%H%M")

def current_date():
    ''' return format: YYYY-mm-dd HH:mm:ss '''
    return strftime("%Y-%m-%d %H:%M:%S")



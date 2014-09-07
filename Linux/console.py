
import os
import re
import PyUtils
from PyUtils.strings import clean_new_line
__regexp_command_not_found = re.compile("/^(command\snot\sfound)/")

        
def run_command(command):
    """ execute command """
    res = list(os.popen(command))
    if not res: return False
    
    match = __regexp_command_not_found.match(res[0])
    
    if not match:
        if len(res) > 1: 
            return [clean_new_line(s) for s in res]
        else: 
            return clean_new_line(res[0])
    return False
    
    
def colored(text, color):
    ''' return colored text'''
    if color == 'red'    :  col = '\033[91m'
    elif color == 'green':  col = '\033[92m'
    elif color == 'blue' :  col = '\033[94m'
    else: return text
    return col + text + '\033[0m'


def binary_exists(binary):
    """ return boolean """
    res = run_command('which %s' % binary)
    if res and not res.startswith('which: no'):
        return True
    return False
        
        

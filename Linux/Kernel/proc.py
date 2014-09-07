from Linux import IO
from Linux import console
import os


def __parse_status_file(filePointer):
    """ parse pid status and return into dict """
    # create list
    rl = filePointer.readlines();
    tmp_list = [x.split('\t') for x in rl]
    
    tmp_dict = {}
    for i in tmp_list:
        dict_key = i[0].replace(':','')
        value = i[1].split('\n')[0].replace('\t','').lstrip().rstrip()
        tmp_dict[dict_key] = value
        
    return tmp_dict


def get_pid_status(pid):
    """ return the content of /proc/$pid/status"""
    fileName = "/proc/%d/status" % pid
    fp = IO.open_file(fileName)
    assert fp, "can't open file %s" % fileName
    return __parse_status_file(fp)


def get_pid_open_fd(pid):
    
    fd_list = os.listdir('/proc/%s/fd' % pid)
    tmp_dict = {}
    for i in fd_list:
        tmp_dict[i] = os.path.realpath("/proc/%s/fd/%s" % (pid, i))
        
    return tmp_dict


import Linux.console
import Linux.IO

GROUP_FILE = "/etc/group"

def group_exists(groupname):
    """ return boolean """
    try:
        res = __search(groupname)
        return True
    except:
        return False


def find_by_gid(gid):
    """ return dict or boolean if find didn't match results """
    try:
        return __search(gid)
    except:
        return False


def find_by_name(groupname):
    """ return dict or boolean if find didn't match results """
    try:
        return __search(groupname)
    except:
        return False
    
    

def __search(pattern):
    """ return info about group 
        pattern can be groupname or gid
    """
    cmd = "grep %s %s" % (pattern, GROUP_FILE)
    res = Linux.console.run_command(cmd)
    assert res, "search for %s into group failed" % pattern
    
    tmp_dict = {}
    for i in res:
        info = i.split(':')
        tmp_dict['groupname'] = info[0]
        tmp_dict['gid'] = info[2].replace('\n','')
        
    return tmp_dict
    
    
def create(groupname, gid = ''):
    """ """
    if gid != '':
        if isinstance(gid, int): cmd = "groupadd -g %d %s" % (gid, groupname)
        else: cmd = "groupadd -G %s %s" % (gid, groupname)
        
    return Linux.console.run_command(cmd)


def delete(groupname):
    """ """
    cmd = "groupdel %s ; echo $?" % groupname
    res = Linux.console.run_command(cmd)
    if int(res[0].replace('\n','')) == 0:
        return True
    
    return False
    
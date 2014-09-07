
import sys
import Linux.console
import Linux.IO
    


def is_enabled():
    if get_status() == 'Disabled': 
        return False
    return True


def get_status():
    SESTATUS = Linux.console.run_command('getenforce')
    return SESTATUS


def perm_change_mode(mode):
    se_config = "/etc/security/selinux"
    if Linux.IO.file_exists(se_config):
        print "debug"
    
def temp_change_mode(mode):
    return Linux.console.run_command('setenforce %s' % mode)
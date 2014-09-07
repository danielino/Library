
import os
import Linux.console


def free_space(mountPoint):
    ''' return dict with information about fs '''

    if not os.path.isdir(mountPoint):
        raise Exception("mountpoint %s not exists." % mountPoint)

    cmd = Linux.console.run_command("df -h %s" % mountPoint)

    # get value and return dict
    space = cmd[2].split()
    disk_space = {
        'total' : space[0],
        'used' : space[1],
        'available' : space[2],
        'used_percent' : space[3],
        'mountPoint' : space[4]
    }

    return disk_space


def free_space_all_disks():
    tmp = []
    for i in list_all_disks():
        tmp.append(free_space(i))        
    return tmp


def list_all_disks():
    """ """
    
    
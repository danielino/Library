import Linux.console
import Linux.group
import crypt


def user_exists(username):
    """ return boolean """
    users = get_all_user()
    
    for i in users:
        if username in i:
            return True
        
    return False


def get_all_user():
    """ return list """
    assert Linux.console.binary_exists('cut'), "cut binary not found"
    user = Linux.console.run_command("cat /etc/passwd | cut -d ':' -f1")
    return [x.replace('\n','') for x in user ]


def get_user_info(username):
    """ return dict with name,uid,gid,home,shell of the user"""
    assert Linux.console.binary_exists('egrep'), "egrep binary not found"
    info = Linux.console.run_command("cat /etc/passwd |egrep '^%s\:'" % username)
    if not info:
        return False
    
    user = info[0].split(':')

    user_dict = {
         'name' : user[0],
         'uid' : user[2],
         'gid' : user[3],
         'home' : user[5],
         'shell' : user[6].replace('\n','')
    }
    return user_dict
    
    
def find_by_uid(uid):
    """ return dict or raise Assert Exception if user cannot be found """
    user = Linux.console.run_command("cat /etc/passwd |egrep %s" % uid)
    assert user, "can't find user with uid: %s" % uid
    
    username = user.split(':')[0]
    return get_user_info(username)


def create(username, password, groups='', home = "", shell="/bin/bash"):
    """ return boolean. create user """
    if groups != "" and not Linux.group.group_exists(groups):
        Linux.group.create(groups)
    else:
        groups = username
        if not Linux.group.group_exists(groups): 
            Linux.group.create(groups)
        
    if home == "": home = "/home/%s" % username
    
    string = "adduser  -g {groups} -m -d {home} -s {shell} -p {pass} {username} ; echo $?"
        
    fmt_dict = {
        "groups" : groups, 
        "home" : home,
        "pass" : crypt.crypt(password,'wtf'),
        "shell" : shell, 
        "username" : username 
    }
    res = Linux.console.run_command(string.format(**fmt_dict))

    # res == false because the run_command function return false if the return 
    # string is empty (os.popen())
    if int(res[0].replace('\n','')) == 0: return True
    if not res.endswith('already exists'): return True
    
    return False
       
    
def delete(username):
    """ return boolean. delete user """
    cmd = "userdel -f -r %s ; echo $?" % username
    res = Linux.console.run_command(cmd)
    
    # check the return value of the last command executed
    if int(res[0].replace('\n','')) == 0: 
        return True
    return False
    
    
    
def change_password(username, newpw):
    """ change password of user """
    cmd = "%s:%s | chpasswd" % (newpw, username)
    return Linux.console.run_command(cmd) 
    

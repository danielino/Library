
import Linux.console

def is_registered():
    if Linux.console.run_command("rhn_check") == "":
        return True
    return False


def register(rhn_username, rhn_password, system_proxy=""):
    if is_registered():
        raise Exception("This System is already registered with rhn")
    
    if system_proxy == "":
        str = "rhnreg_ks --username={username} --password={password}".format(username=rhn_username, password=rhn_password)
    else:
        str = "rhnreg_ks --username={username} --password={password} --proxy={proxy}".format(username=rhn_username, password=rhn_password, proxy=system_proxy)
        
    return Linux.console.run_command(str)
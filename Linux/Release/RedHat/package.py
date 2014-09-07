
import yum

yb = yum.YumBase()

    
def is_installed(pkg_name):
    if yb.rpmdb.searchNevra(name=pkg_name): 
        return True
    return False


def return_package_installed():
    pkgs = yb.rpmdb.getPkgList()
    tmp = []
    for i in pkgs:
        tmp.append({
                    'name' : i[0],
                    'arch' : i[1],
                    'version' : i[2],
                    'release' : i[3]
                    })
        
    return tmp


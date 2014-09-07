
import os
import Linux
import re

re_ok = re.compile('.+(OK).+')

def service_exists(service_name):
    if os.path.isfile("/etc/init.d/%s" % service_name):
        return True
    return False


def __action(service_name, action):
    if not service_exists(service_name):
        if Linux.EXCEPTION_ENABLED: 
            raise Exception("service not found")
        return False
    res = Linux.console.run_command("/etc/init.d/%s %s" % (service_name, action))
    if re_ok.findall(res): 
        return True

    return False

    
def start(service_name):
    if service_is_started(service_name):
        if Linux.EXCEPTION_ENABLED:
            raise Exception("service is already started")
        return False
    
    return __action(service_name, 'start')


def stop(service_name):
    return __action(service_name, 'stop')


def restart(service_name):
    return __action(service_name, 'restart')


def status(service_name):
    if service_is_started(service_name):
        return 'started'
    return 'stopped'


def reload(service_name):
    return __action(service_name, 'reload')


def service_is_started(service_name):
    if Linux.process.get_pid(service_name):
        return True
    return False
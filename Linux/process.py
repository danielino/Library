import Linux.console
from Linux.Kernel import proc

def get_pid(p_name):
    """ """
    pid = Linux.console.run_command("pgrep -f %s" % p_name)
    if not pid:
        return False
    pid_list = [int(x.split('\n')[0]) for x in pid]
    if len(pid_list) == 1: return pid_list[0]
    return pid_list


def pgrep_get_status(p_name):
    """ search for process match the p_name string and return the parsed status of process in proc/$(pid)/status
        if multiple pid found, return a list of dict, else return dict
        this function use proc module and parsing data from /proc filesystem
    """
    pid = get_pid(p_name)
    if isinstance(pid, list) and len(pid) > 1:
        tmp = []
        for i in pid:
            tmp.append(proc.get_pid_status(i))

        return tmp
    else:
        return proc.get_pid_status(pid)


def get_pid_fd_open(p_name):
    return proc.get_pid_open_fd(get_pid(p_name))


def kill_process(p_name, signal="-15"):
    """ kill process. default signal is SIGTERM """
    return Linux.console.run_command("kill %s %s" % (signal, p_name))


def kill_process_forced(p_name):
    """ sending SIGKILL """
    return kill_process(p_name, '-9')
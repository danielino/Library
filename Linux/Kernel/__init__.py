from Linux.Kernel import proc
import Linux.console

version = Linux.console.run_command('uname -r')

def get_versions():
    """ @return string version """
    return version



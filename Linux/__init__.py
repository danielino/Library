import platform

# modules
import console
import group
import IO
import process
import service
import user


# package
import Device
import Kernel
import Release
import Security
import Storage        
        

# Module config
EXCEPTION_ENABLED = True

# System info
hostname = platform.node()
linux_distribution = platform.linux_distribution()
arch = platform.machine()

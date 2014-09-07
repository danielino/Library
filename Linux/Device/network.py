# all_interfaces found on <http://code.activestate.com/recipes/439093/#c1>
# modified by Daniele Marcocci
#
# List of change:
#    change return type from tuple to dictionary
#    added  hwaddr infointo dictionary
#    @TODO: add gateway and subnect mask (in cifr format) to all_interface array of dict return


import socket
import fcntl
import struct
import array
import Linux
 
def __format_ip(addr):
    return str(ord(addr[0])) + '.' + \
           str(ord(addr[1])) + '.' + \
           str(ord(addr[2])) + '.' + \
           str(ord(addr[3]))
           
def all_interfaces():
    """ return list of dict with network information (iface_name, ipv4, hwaddr)"""
    max_possible = 128  # arbitrary. raise if needed.
    _bytes = max_possible * 32
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    names = array.array('B', '\0' * _bytes)
    outbytes = struct.unpack('iL', fcntl.ioctl(
        s.fileno(),
        0x8912,  # SIOCGIFCONF
        struct.pack('iL', _bytes, names.buffer_info()[0])
    ))[0]
    namestr = names.tostring()
    lst = []
    for i in range(0, outbytes, 40):
        name = namestr[i:i+16].split('\0', 1)[0]
        ip   = namestr[i+20:i+24]
        info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', name))
        hwaddr = ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]
        lst.append(
                   { 'name' : name, 
                     'ip'   : __format_ip(ip), 
                     'addr' : hwaddr
                   })
    s.close()
    return lst
 
 
def get_iface_info(iface):
    """ @return dict with network information (iface_name, ipv4, hwaddr)"""
    for i in all_interfaces():
        if i['name'] == iface: 
            return i
    if Linux.EXCEPTION_ENABLED:
        raise Exception("can't find interface %s" % iface)
    return False
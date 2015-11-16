#!/usr/bin/python
import VmInclude


def main():
    host = "127.0.0.1"
    port = ":8443"
    username = raw_input('username? ')
    password = raw_input('password? ')

    hostconnection = VmInclude.connectToHost(host + port, username, password)

    webserver = hostconnection.get_vm_by_name("Ubuntu 64-bit - webserver")
    if webserver.is_powered_off():
        print('Info: VM webserver already off - nothing to do here')
    else:
        print('Info: Powering off VM webserver')
        webserver.power_off()

    bigip1 = hostconnection.get_vm_by_name("v11.6-1")
    if bigip1.is_powered_off():
        print('Info: VM v11.6-1 already off - nothing to do here')
    else:
        print('Info: Powering off VM v11.6-1')
        bigip1.power_off()

    bigip2 = hostconnection.get_vm_by_name("v11.6-2")
    if bigip2.is_powered_off():
        print('Info: VM v11.6-2 already off - nothing to do here')
    else:
        print('Info: Powering off VM v11.6-2')
        bigip2.power_off()

if __name__ == '__main__':
    main()
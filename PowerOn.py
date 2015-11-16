#!/usr/bin/python
import time
import VmInclude


def main():
    host = "127.0.0.1"
    port = ":8443"
    username = raw_input('username? ')
    password = raw_input('password? ')

    hostconnection = VmInclude.connectToHost(host + port, username, password)
    startWebServer(hostconnection)
    startLoadBalancer(hostconnection)


def startLoadBalancer(hostConnection):
    bigip1 = hostConnection.get_vm_by_name("v11.6-1")
    if bigip1.is_powered_on():
        print('Info: VM v11.6-1 already powered on')
    else:
        print('Info: Powering on VM v11.6-1')
        bigip1.power_on()

    bigip2 = hostConnection.get_vm_by_name("v11.6-2")
    if bigip2.is_powered_on():
        print('Info: VM v11.6-2 already powered on')
    else:
        print('Info: Powering on VM v11.6-2')
        bigip2.power_on()


def guestLogin(server, username, password):
    try:
        print('Info: Attempting to login to guest OS')
        server.login_in_guest("mrajagopal", "Srinivas600")

    except VmInclude.VIException as err:
        print('Error: ' + str(err))


def startWebServer(hostConnection):
    webserver = hostConnection.get_vm_by_name("Ubuntu 64-bit - webserver")
    if webserver.is_powered_on():
        print('Info: VM webserver already powered on')
    else:
        print('Info: Powering on VM webserver')
        webserver.power_on()


if __name__ == '__main__':
    main()

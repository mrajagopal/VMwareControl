#!/usr/bin/python
import VmInclude

def main():
    host = "127.0.0.1"
    port = ":8443"
    username = raw_input('username? ')
    password = raw_input('password? ')


    #connect to host
    try:
        hostconnection = VmInclude.connectToHost(host+port, username, password)
        print("Type: ", hostconnection.get_server_type())
        print(hostconnection.get_registered_vms())
        print(hostconnection.get_clusters())
        print('API Type: ' + hostconnection.get_api_type() + ' API Version: ', hostconnection.get_api_version())
        print(hostconnection.get_resource_pools())
        print(hostconnection.get_datacenters())
        webserver = hostconnection.get_vm_by_name('Ubuntu 64-bit - webserver');
        print(webserver.get_snapshots())
        hostconnection.disconnect()

    except VmInclude.VIApiException as err:
        print(err)


if __name__ == '__main__':
    main()

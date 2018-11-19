from bluedot.btcomm import BluetoothClient
from signal import pause


def data_received(data):
    print(data)


c = BluetoothClient("j2controller", data_received)
c.send("helloworld")

pause()


# from bluedot.btcomm import BluetoothServer
# from signal import pause

# def data_received(data):
#    print(data)
#    s.send(data)

#s = BluetoothServer(data_received)
# pause()

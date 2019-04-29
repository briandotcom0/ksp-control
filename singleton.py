import time
import krpc


conn=None
vessel=None
ip=None

def init():
    conn=None
    vessel=None
    ip=None


def getIP():
    return ip

def getConn():
    while conn is None:  # while no connection to kRPC server, try every 15 secs
        try:
            conn = krpc.connect(
                name='KCP',
                address='192.168.0.209',
                rpc_port=50000, stream_port=50001)
        except ConnectionRefusedError:
            print("Is KSP running?")
        time.sleep(15)
    return conn

def getVessel():
    if vessel is None:
        vessel=conn.space_center.active_vessel
    return vessel


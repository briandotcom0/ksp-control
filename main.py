import krpc
import time
import callbacks

conn = None

while conn is None:  # while no connection to kRPC server, try every 15 secs
    try:
        conn = krpc.connect(
            name='KCP',
            address='192.168.1.134',
            rpc_port=50000, stream_port=50001)
    except ConnectionRefusedError:
        print("Is KSP running?")
    time.sleep(15)

vessel = conn.space_center.active_vessel
callbacks.setup(conn, vessel)

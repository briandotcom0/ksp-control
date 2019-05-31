import time
import krpc
import callbacks
import pins

class Singleton:

    conn=None
    vessel=None
    ip=None
    callback = None
    pin = None

    def init(self):
        self.conn=None
        self.vessel=None
        self.ip=None
        self.callback=callbacks.Callbacks()
        self.pin=pins.Pins()
        self.callback.init(self, self.pin)


    def getIP(self):
        return self.ip

    def getConn(self):
        while self.conn is None:  # while no connection to kRPC server, try every 15 secs
            try:
                self.conn = krpc.connect(
                    name='KCP',
                    address='192.168.0.209',
                    rpc_port=50000, stream_port=50001)
            except ConnectionRefusedError:
                print("Is KSP running?")
            time.sleep(15)
        return self.conn

    def getVessel(self):
        if self.vessel is None:
            self.vessel=self.conn.space_center.active_vessel
        return self.vessel


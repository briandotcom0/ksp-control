import time
import krpc
import callbacks
import pins
import i2c

class Singleton:

    conn=None
    vessel=None
    ip=None
    callback = None
    pin = None
    i2c=None

    def init(self):
        self.conn=None
        self.vessel=None
        self.ip=None
        self.callback=callbacks.Callbacks()
        self.pin=pins.Pins()
        self.callback.init(self, self.pin)
        self.i2c=i2c.I2C()
        self.i2c.init(self)

    def clean(self):
        self.i2c.clean()
        self.pin.cleanup()
        self.conn.close()


    def getIP(self):
        if self.ip is None:
            self.ip='192.168.0.209'
        return self.ip

    def getConn(self):
        while self.conn is None:  # while no connection to kRPC server, try every 15 secs
            try:
                self.conn = krpc.connect(
                    name='KCP',
                    address=self.ip,
                    rpc_port=50000, stream_port=50001)
            except ConnectionRefusedError:
                print("Is KSP running?")
            time.sleep(15)
        return self.conn

    def getVessel(self):
        if self.vessel is None:
            self.vessel=self.conn.space_center.active_vessel
        return self.vessel


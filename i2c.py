import singleton
import I2C_LCD_driver
import threading
import time


class I2C:

    disp=None
    lines=None
    single=None
    thread1=None
    thread1r=0

    def init(self, sig):
        self.disp=I2C_LCD_driver.lcd
        self.single=sig
        self.lines=[]
        self.thread1=threading.Thread(target=threaded, args=self)
        self.thread1r=1
        self.thread1.start()

    def clean(self):
        self.thread1r=0

    def format(n):
        ct=0
        while n>1000:
            n/=1000
            ct+=1
        suffx=['','K','M','G','T','P','E']
        return str(n)[0:4].rstrip(['.'])+suffx[ct]

    def threaded(self):
        conn=self.single.getConn()
        while self.thread1r==1:
            vessel=conn.space_center.active_vessel
            flight=vessel.flight()
            orb=vessel.orbit()
            self.disp.lcd_clear()
            self.disp.lcd_display_string("MSL: "+flight.mean_altitude, 1)
            self.disp.lcd_display_string("m/s: "+format(flight.speed)+" "+format(orb.speed), 2)
            self.disp.lcd_display_string("a/p: "+format(orb.apoapsis)+" "+format(orb.periapsis), 3)
            time.sleep(1)




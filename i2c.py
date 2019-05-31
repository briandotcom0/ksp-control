import singleton
import I2C_LCD_driver
import threading


class I2C:

    disp=None
    lines=None
    single=None

    def init(self, sig):
        self.disp=I2C_LCD_driver.lcd
        self.single=sig
        self.lines=[]

    def format(n):
        ct=0
        while n>1000:
            n/=1000
            ct+=1
        suffx=['','K','M','G','T','P','E']
        return str(n)[0:4].rstrip(['.'])+suffx[ct]

    def threaded(self):
        conn=self.single.getConn()
        vessel=conn.space_center.active_vessel
        flight=vessel.flight()
        orb=vessel.orbit()
        self.disp.lcd_clear()
        self.disp.lcd_display_string("MSL: "+flight.mean_altitude, 1)
        self.disp.lcd_display_string("m/s: "+format(flight.speed)+" "+format(orb.speed), 2)
        self.disp.lcd_display_string("a/p: "+format(orb.apoapsis)+" "+format(orb.periapsis), 3)




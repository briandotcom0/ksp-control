import krpc
import time
import callbacks
import singleton

singleton.init()
callbacks.init()
# conn = None

vessel = singleton.getVessel()
callbacks.setup(conn, vessel)

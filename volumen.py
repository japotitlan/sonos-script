#
#   Script basico para mantener el mismo volumen
#

import soco
device = soco.discovery.any_soco()

while(True):
    device.volume = 25
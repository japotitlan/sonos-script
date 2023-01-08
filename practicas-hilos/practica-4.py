#
# Primer prototipo funcional de asignacion de volumen automatica
#

import threading,time,soco

device = soco.discovery.any_soco()

global stop
stop = False

global volumen
volumen = 25

def AjustarVolumen():
    
    global stop
    global volumen

    while not stop:
        #print(volumen)
        device.volume = volumen
        time.sleep(0.01)


def main():
    global volumen
    global stop

    hilo = threading.Thread(target=AjustarVolumen)
    hilo.start()

    while volumen != 0:

        print(f'\nVolumen actual [%{volumen}]')
        volumen = int(input('Ingrese volumen 0-100: '))

    stop = True


if __name__ == '__main__':
    main()
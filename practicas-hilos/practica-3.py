import threading,time

global stop
stop = False

global volumen
volumen = 25

def AjustarVolumen():
    
    global stop
    global volumen

    while not stop:
        #device.volume = 25
        print(volumen)
        time.sleep(1)


def main():
    global volumen
    global stop

    hilo = threading.Thread(target=AjustarVolumen)
    hilo.start()

    volumen = int(input())

    time.sleep(5)
    stop = True


if __name__ == '__main__':
    main()


# for i in range(500):
#     volumen = int(input())
#     volumen_evento.set()

#     hilo = threading.Thread(target=AjustarVolumen, args=(volumen,))
#     hilo.start()

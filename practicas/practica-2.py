#
# Practica para comprender el uso de eventos en threading
#

import threading,time

pause_resume_event = threading.Event()
stop_event = threading.Event()

def analizar():
    for x in range(1000):
        if stop_event.is_set():
            print('patucasa maboy')
            return
        else:
            pause_resume_event.wait()
            print(x)
            time.sleep(0.5)

hilo = threading.Thread(target=analizar)
hilo.start()

input('Ingresa [p] para pausar/resumir\nIngresa [x] para salir\n\nEnter para Comenzar...')

pause_resume_event.set()

while True:
    comando = input()

    if comando == 'x':
        stop_event.set()
        exit()
    elif comando == 'p':
        if pause_resume_event.is_set():
            pause_resume_event.clear()
            time.sleep(0.3)
            print('--------\nPAUSADO\n--------')
        else:
            print('---------\nREANUDAR\n--------')
            time.sleep(0.3)
            pause_resume_event.set()

# importar librerias para poder manejar hilos y otra para poder detener procesos
import threading,time

# funcion que se ejecutara en el hilo
def funcion_hilo():
    print('empezando')
    time.sleep(3)
    print('saliendo')

# hilo relacionado a la funcion
hilo = threading.Thread(target=funcion_hilo)

# checar si el hilo está activo - False
print(hilo.is_alive())

# iniciar el hilo, ejecutando la funcion
hilo.start()

# checar si el hilo activo - True
print()
print(hilo.is_alive())
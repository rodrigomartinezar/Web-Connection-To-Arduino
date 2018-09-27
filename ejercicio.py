import serial
import time
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
try:
    while True:
        data = mysock.recv(512)
        if(len(data) < 1):
            break
        data_decoded = data.decode()
        byte_to_string = str(data_decoded)
        string_separado = byte_to_string.split(' ')
        # print(string_separado)
        arduino = serial.Serial('COM6', 9600)
        time.sleep(2)
        if string_separado[1] == '200':
            print("Mandando 'h' --> Prendiendo LED")
            arduino.write(b'h')
            time.sleep(2)
        if string_separado[1] == '404':
            # print("No se pillo en la vuelta ", contador)
            print("Mandando cualquiera --> Apagando LED")
            arduino.write(b'z')
            time.sleep(2)
        arduino.close()
    mysock.close()
except Exception as error:
    print(str(error))

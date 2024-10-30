import socket

# El cliente se conecta al servidor, recibe la información y la muestra.

# Configurar el cliente (TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))  # Conectarse al servidor

# Recibir y mostrar la respuesta del servidor
response = client_socket.recv(1024)
print("Respuesta del servidor:\n", response.decode())

# Cerrar la conexión
client_socket.close()

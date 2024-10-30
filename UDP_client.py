import socket

# El cliente envía un mensaje al servidor y recibe la hora actual.


# Configurar el cliente (UDP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviar un mensaje al servidor
server_address = ('localhost', 12345)
message = "¿Cuál es la hora actual?"
client_socket.sendto(message.encode(), server_address)

# Recibir la respuesta del servidor
response, _ = client_socket.recvfrom(1024)
print("Respuesta del servidor:", response.decode())

# Cerrar el socket
client_socket.close()


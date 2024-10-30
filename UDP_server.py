import socket
from datetime import datetime


# Este servidor puede responder la hora actual a cada cliente que le envíe un mensaje.

# Configurar el servidor (UDP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))

print("Servidor UDP esperando mensajes...")

while True:
    # Recibir datos de un cliente
    data, client_address = server_socket.recvfrom(1024)  # Tamaño máximo de mensaje: 1024 bytes
    print(f"Mensaje recibido de {client_address}: {data.decode()}")

    # Responder al cliente
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"Hora actual: {current_time}"
    server_socket.sendto(message.encode(), client_address)

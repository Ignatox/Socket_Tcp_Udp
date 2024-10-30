import socket
from datetime import datetime

# Este servidor proporcionará la hora actual y el número de conexiones realizadas por los clientes.
 
# Configurar el servidor (TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))  # Enlazar a dirección y puerto
server_socket.listen(5)  # Escuchar hasta 5 conexiones entrantes

print("Servidor TCP esperando conexiones...")
connections = 0

while True:
    # Aceptar la conexión de un cliente
    client_socket, client_address = server_socket.accept()
    connections += 1
    print(f"Conexión aceptada de {client_address}. Total de conexiones: {connections}")
    
    # Enviar información al cliente
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"Hora actual: {current_time}\nConexiones: {connections}"
    client_socket.sendall(message.encode())  # Enviar mensaje codificado

    # Cerrar la conexión
    client_socket.close()

# Socket_Tcp_Udp
 Repositorio creado para la realización del trabajo práctico de programación de capa de transporte de redes de datos.

#### Explicación:
- TCP (orientado a la conexión):
    - Servidor TCP: Escucha en el puerto 12345 y acepta conexiones de los clientes. Una vez conectado un cliente, el servidor envía la hora actual y el número de conexiones realizadas.
    - Cliente TCP: Se conecta al servidor en localhost:12345 y recibe la información enviada por el servidor.
- UDP (sin conexión):
    - Servidor UDP: Escucha mensajes de cualquier cliente en el puerto 12345 y responde con la hora actual.
    - Cliente UDP: Envía un mensaje al servidor preguntando la hora actual y recibe la respuesta sin necesidad de una conexión previa.
    
Elegir entre TCP o UDP:
TCP es ideal si necesitas un servicio confiable, donde los datos deben llegar completos y en orden.
UDP es útil para aplicaciones que no requieren confirmación de entrega (como transmisión de video o juegos en línea), ya que es más rápido y no necesita establecer una conexión formal.
Ambos enfoques cumplen el objetivo de proporcionar un servicio de comunicación entre aplicaciones, ya sea confiable (TCP) o sin conexión (UDP).

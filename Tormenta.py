import socket
import threading
import re
import email

# Palabras que suelen aparecer en los mensajes de spam
pam_words = ["oferta", "gratis", "urgente", "dinero"]

# Expresiones regulares para detectar mensajes de spam
spam_subject_patterns = [
    re.compile("(?i).*(oferta|gratis|urgente|dinero).*"),
    re.compile(".*@[a-zA-Z0-9]+.(com|net|org).*"),
    re.compile(".*(sitio web sospechoso|archivo adjunto peligroso).*"),
]

# Expresiones regulares para detectar ataques de DoS
dos_patterns = [
    re.compile(".*"),
    re.compile(".*"),
    re.compile(".*"),
]

def is_spam(message):
    subject = message.get("Subject")
    for word in spam_words:
        if word in subject:
            return True
    return False

def is_dos(address):
    for pattern in dos_patterns:
        if pattern.search(address):
            return True
    return False

def handle_client(client_socket):
    # Recibir los datos del cliente
    data = client_socket.recv(1024)

    # Verificar si los datos son spam o DoS
    if is_spam(data):
        # Bloquear al cliente
        client_socket.close()
        return
    if is_dos(client_socket.getsockname()[0]):
        # Bloquear al cliente
        client_socket.close()
        return

    # Enviar una respuesta al cliente
    client_socket.send("Mensaje recibido correctamente")

def main():
    # Crear un socket servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 22))
    server_socket.listen(5)

    # Escuchar las conexiones entrantes
    while True:
        client_socket, address = server_socket.accept()

        # Crear un hilo para cada cliente
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    main()

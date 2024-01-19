import email
import socket

# Crea un objeto de socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conéctate al servidor
server_address = ('127.0.0.2', 80)  # Reemplaza esto con la dirección del servidor
client_socket.connect('127.0.0.1')

# Crea una lista de palabras que indican spam
spam_words = ["oferta", "gratis", "urgconnect(): AF_INET address must be tuple, not strente", "dinero"]

# Define una función para verificar si un mensaje es spam
def is_spam(message):
    # Convierte el mensaje a un objeto de tipo dict
    message_dict = email.message_from_string(message)
    # Obtiene el asunto del mensaje
    subject = message_dict.get("Subject")
    # Itera sobre la lista de palabras que indican spam
    for word in spam_words:
        if word in subject:
            return True
    return False

# Define la variable 'juan'
juan = "Juan Pérez <juan.perez@gmail.com>"

# Crea un mensaje de correo electrónico para enviar al servidor
message = f"""Subject: Oferta increíble
From: {juan}
To: Ana García <ana.garcia@hotmail.com>

Hola Ana,

Te escribo para contarte sobre esta oferta increíble que encontré en esta página web: https://ofertasincreibles.com

Solo tienes que ingresar tus datos personales y bancarios y podrás acceder a un premio de un millón de dólares. No dejes pasar esta oportunidad única, es totalmente seguro y confiable.

Espero tu respuesta pronto.

Saludos,
{juan}
"""

# Verifica si el mensaje es spam
if is_spam(message):
    # Envía una respuesta indicando que el mensaje es spam
    response = "Tu mensaje ha sido identificado como spam y ha sido rechazado.\n"
    client_socket.send(response.encode("utf-8"))
else:
    # Envía el mensaje al servidor
    client_socket.send(message.encode("utf-8"))

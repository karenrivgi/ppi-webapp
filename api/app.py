from unidecode import unidecode
from flask import Flask, render_template, request

# Instanciar un objeto de clase Flask
app = Flask(__name__)

# Identificar la ruta de la app
@app.route('/', methods=['GET', 'POST'])
def encrypt():

    # Si se presionó un botón
    if request.method == 'POST':
        # Obtener el texto ingresado por el usuario
        text = request.form['word-input']

        #Se utiliza la función unidecode para eliminar tildes y caracteres especiales del texto
        clean_text = unidecode(text)

        # Obtener la clave seleccionada por el usuario
        key = int(request.form['clave'])

        # Conocer qué botón fue el que se presionó
        mode = request.form['encryption-mode']

        if mode == "CIFRAR":
            # Realizar el cifrado César
            result_text = encrypt_cesar(clean_text, key)
        else: 
            # Descifrar el mensaje
            result_text = decrypt_cesar(clean_text, key)

        # Renderizar la plantilla HTML con el resultado, y dejar los valores anteriores seleccionados
        return render_template('index.html', result_text=result_text, text_input=text, selected_key=key)

    # Renderizar la plantilla HTML inicial y el valor de la clave en 3 por defecto.
    return render_template('index.html', selected_key=3)


def encrypt_cesar(text, key):
    """
    Función para cifrar un texto utilizando el cifrado César.

    Parameters:
    - text (str): El texto a cifrar.
    - key (int): La clave de cifrado.

    Returns:
    - encrypted_text (str): El texto cifrado.
    """
    encrypted_text = ""

    # Recorremos el texto cifrando cada letra
    for char in text:
        if char.isalpha():
            if char.islower():
                # Cifrado de caracteres en minúsculas
                encrypted_text += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            else:
                # Cifrado de caracteres en mayúsculas
                encrypted_text += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else: 
            # Caracteres no alfabéticos se mantienen iguales
            encrypted_text += char
    return encrypted_text


def decrypt_cesar(text, key):
    """
    Función para descifrar un texto cifrado utilizando el cifrado César.

    Parameters:
    - text (str): El texto cifrado.
    - key (int): La clave de cifrado utilizada.

    Returns:
    - decrypted_text (str): El texto descifrado.
    """

    decrypted_text = ""
    # Recorremos el texto descifrando cada letra
    for char in text:
        if char.isalpha():
            if char.islower():
                # Descifrado de caracteres en minúsculas
                decrypted_text += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
            else:
                # Descifrado de caracteres en mayúsculas
                decrypted_text += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
        else:
            # Caracteres no alfabéticos se mantienen iguales
            decrypted_text += char

    return decrypted_text




import random
import string
import hashlib
import os

# Función para generar una contraseña personalizada
def generar_contraseña_personalizada():
    letras = random.sample(string.ascii_letters, 4)
    numeros = random.sample(string.digits, 4)
    caracteres_especiales = random.sample(string.punctuation, 2)
    contraseña = letras + numeros + caracteres_especiales
    random.shuffle(contraseña)
    return ''.join(contraseña)

# Función para generar múltiples contraseñas
def generar_contraseñas_personalizadas(num_contraseñas=15):
    return [generar_contraseña_personalizada() for _ in range(num_contraseñas)]

# Función para combinar caracteres de contraseñas generadas
def combinar_caracteres(contraseñas, posicion=7):
    caracteres = [contraseña[posicion] for contraseña in contraseñas if len(contraseña) > posicion]
    return ''.join(caracteres)

# Función para hash con salting
def hash_password(password):
    salt = os.urandom(16)
    hash_obj = hashlib.sha256(salt + password.encode())
    hashed_password = hash_obj.hexdigest()
    return salt, hashed_password

# Verificar la contraseña
def verify_password(stored_hash, stored_salt, password_attempt):
    hash_obj = hashlib.sha256(stored_salt + password_attempt.encode())
    attempt_hash = hash_obj.hexdigest()
    return attempt_hash == stored_hash

# Generar 15 contraseñas personalizadas y combinar
contraseñas = generar_contraseñas_personalizadas()
contraseña_final = combinar_caracteres(contraseñas)

# Aplicar hashing y salting a la contraseña final
salt, hashed_contraseña_final = hash_password(contraseña_final)
print("Salt:", salt.hex())
print("Hashed contraseña final:", hashed_contraseña_final)

# Verificación de la contraseña final
contraseña_intento = contraseña_final  # Prueba con la contraseña original
es_correcta = verify_password(hashed_contraseña_final, salt, contraseña_intento)
print("¿Contraseña correcta?", es_correcta)

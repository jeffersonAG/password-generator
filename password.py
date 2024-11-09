import random
import string

def generar_contraseña_personalizada():
    # Elegir 4 letras aleatorias (mayúsculas o minúsculas)
    letras = random.sample(string.ascii_letters, 4)
    
    # Elegir 4 números únicos aleatorios
    numeros = random.sample(string.digits, 4)
    
    # Elegir 2 caracteres especiales
    caracteres_especiales = random.sample(string.punctuation, 2)
    
    # Combinar y mezclar los caracteres
    contraseña = letras + numeros + caracteres_especiales
    random.shuffle(contraseña)
    
    return ''.join(contraseña)

def generar_contraseñas_personalizadas(num_contraseñas=15):
    contraseñas = [generar_contraseña_personalizada() for _ in range(num_contraseñas)]
    return contraseñas

def combinar_octavos(contraseñas):
    # Tomar el octavo carácter de cada contraseña
    octavos = [contraseña[7] for contraseña in contraseñas if len(contraseña) >= 8]
    return ''.join(octavos)

# Generar 7 contraseñas personalizadas
contraseñas = generar_contraseñas_personalizadas()
print("Contraseñas generadas:")
for i, contraseña in enumerate(contraseñas, 1):
    print(f"{i}: {contraseña}")

# Generar la contraseña final combinada con el octavo carácter de cada contraseña
contraseña_final = combinar_octavos(contraseñas)
print("\nContraseña final combinada:", contraseña_final)

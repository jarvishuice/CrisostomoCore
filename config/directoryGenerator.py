import os

# Crear directorios del 1 al 999
for i in range(1, 1000):
    os.makedirs(f'C://CrisostomoCore/Media/Books/{i}', exist_ok=True)

print("Directorios creados exitosamente.")

# suscriptores.py

print("**** Lista de suscriptores ****\n")
suscriptores = set()

# 1. Registro inicial
try:
    numero = int(input("¿Cuántos suscriptores deseas registrar? "))
except ValueError:
    print("⚠️  Debes escribir un número entero.")
    quit()

for _ in range(numero):
    suscriptores.add(input("Nuevo suscriptor: ").strip())

# 2. Nuevo intento de suscripción
nuevo = input("\nProporciona un nuevo suscriptor: ").strip()
if nuevo in suscriptores:
    print("Ese suscriptor ya está registrado.")
else:
    suscriptores.add(nuevo)

# 3. Eliminación de suscriptor
eliminar = input("\n¿Qué suscriptor deseas eliminar? ").strip()
if eliminar in suscriptores:
    suscriptores.remove(eliminar)
else:
    print("Ese suscriptor no está en la lista, no se ha eliminado nada.")

# 4. Mostrar resultado final
print("\n**** Lista final de suscriptores ****")
for nombre in sorted(suscriptores):
    print("•", nombre)
print(f"Total: {len(suscriptores)}")

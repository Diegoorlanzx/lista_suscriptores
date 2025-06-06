print('**** lista suscriptores ****')

suscriptores = {'luisa@gimail.com','marcos@gmail.com','miguel@gmail.com'}

print(suscriptores)

nuevo= 'javier@gmail.com'

if nuevo in suscriptores:
    print('ya esta')

else:
    suscriptores.add(nuevo)
    print(suscriptores)


eliminar= 'javier@gmail.com'

suscriptores.remove(eliminar)
print(suscriptores)

print(len(suscriptores))

print('**** lista suscriptores ****')

for i in suscriptores:
    print(i)
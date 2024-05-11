system='SO 2'
if system == 'SO 2':
    print ("no es necesario actualiza")
elif  system == 'SO 1' or system == 'SO 3':
    print ("es necesario actualizar")

approved_user_1='julio'
approved_user_2='carlos'

user='andres'

if user==approved_user_1 or user==approved_user_2:
    print('este usuario tiene acceso a este dispositivo')
else:
    print('este usuario no tiene acceso a este dispositivo')
lista_aprovados=('julio', 'carlos', 'andres', 'felipe', 'julian') 
Username = 'felipe'
if Username in lista_aprovados:
    print('este usuario esta aprobado')
else:
    print('este usuario no esta aprobado')
horario_org=False
if Username in lista_aprovados and horario_org==True:
    print('Intento de inicio de sesión realizado por un usuario autorizado durante el horario de la organización.')
else:
    print('Nombre de usuario no autorizado o intento de inicio de sesión realizado fuera del horario de la organización.')

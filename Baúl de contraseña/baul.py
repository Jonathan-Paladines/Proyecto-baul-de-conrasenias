from datetime import datetime

def user():
    print("=============================\n=============================")
    Nom_user=input("Escriba nombre de usuario: ")
    con_user=input("Escriba Contraseña de usuario: ")
    print("=============================\n=============================")
    
    dic1={Nom_user:con_user}
    print(dic1)
    return(dic1)

def registro():
    print(' DATOS A REGISTRAR')
    PLATAFORMA=input('Ingrese el nombre o url de la plataforma utilizada: ')
    USUARIO= input('Ingrese el usuario utilizado para entrar a la plataforma: ')
    CONTRASEÑA= input('Ingrese la contraseña que usó para la plataforma: ')
    PARA_RECORDAR= input('Escriba una recordatorio en caso de olvidar la contraseña almacenada: \n')
    print('\n')
    DATOS=[PLATAFORMA,USUARIO,CONTRASEÑA,PARA_RECORDAR]
    return (DATOS)

def ver():
    leer_archivo = open ('atad.txt','r')
    mensaje = leer_archivo.read()
    print(mensaje)
    leer_archivo.close()
    return ("Procesando")

def editar():
    print(' Añadiendo nuevas credenciales')
    PLATAFORMA=input('Ingrese el nombre o url de la plataforma utilizada: ')
    USUARIO= input('Ingrese el usuario utilizado para entrar a la plataforma: ')
    CONTRASEÑA= input('Ingrese la contraseña que usó para la plataforma: ')
    PARA_RECORDAR= input('Escriba una recordatorio en caso de olvidar la contraseña almacenada: \n')
    print('\n')
    DATOS1=[PLATAFORMA,USUARIO,CONTRASEÑA,PARA_RECORDAR]
    return (DATOS1)

def eliminar():
    print(' Ja Ja Ja')
    return (4)


val=user()

nombre=input('Por favor ingresa tu nombre: ')
print('Buenos días, ', nombre)
print('A continuación escoge la opción del menú')

print('''
      * * * * * MENU * * * * *
      1.- Registrar nueva contraseña
      2.- Ver contraseñas guardadas
      3.- Editar contraseñas
      4.- Respaldar archivo de contraseñas
      5.- Eliminar Archivo de Contraseña
      6.- Salir
      
      * * * * * * * * * * * * *
      ''')

'''Bloque de validación de opciones de menú''' 
opc=0

while ((opc > 6) or (opc < 1)): 
    
    opc=input('¿Qué opción del menú deseas escoger?: ')
    opc=int(opc)
    
    if ((opc > 6) or (opc < 1)):
        print('Estás escogiendo una opción invalida, vuelve a escoger por favor')
    else:
        print('La opción que escogiste es: ',opc)
                
        
if opc==1:
    print('---> Registrar nueva contraseña')
    now = datetime.now()
    Datitos=registro()
    archi1=open("atad.txt","a")
    archi1.write("\n"+str(now))
    archi1.write("""\n===================================================================\nPLATAFORMA\t\tUSUARIO\t\tCONTRASEÑA\t\tINDICIO\n===================================================================\n""")
    archi1.write(str(Datitos))
    archi1.write("\n===================================================================")
    archi1.close()
    print(Datitos)
elif opc==2:
    print('---> Ver contraseñas guardadas')   
    ver()

    
elif opc==3:
    print('---> Editar contraseñas')
    now = datetime.now()
    Editar=editar()
    edit_archi1 = open('atad.txt','a')
    edit_archi1.write("\n"+str(now))
    edit_archi1.write("""\n===================================================================\nPLATAFORMA\t\tUSUARIO\t\tCONTRASEÑA\t\tINDICIO\n===================================================================\n""")
    edit_archi1.write(str(Editar))
    edit_archi1.write("\n===================================================================")
    edit_archi1.close()
elif opc==4:
    print('RESPALDANDO ARCHIVO DE CONTRASEÑA')
    leer_archivo = open ('atad.txt','r')
    mensaje = leer_archivo.read()
    leer_archivo.close()
    
    now = datetime.now()
    filename1 = datetime.now().strftime("%Y%m%d-%H%M%S")
    resp_archi2 = open(filename1 +'.txt','w')
    resp_archi2.write(mensaje)
    resp_archi2.close()
    
elif opc==5:
    print('---> Eliminar Contraseña')
    eliminar()
    
    """
    with open(r"atad.txt", 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        print("La lineas a borrar son: ", lines)
    """
    
    eliminar_archi1=open("atad.txt","w")
    """eliminar_archi1.write(" ")"""
    eliminar_archi1.close()
    print("Se borraron ",lines," líneas")
    print("\bARCHIVO BORRADO")
else:
    print('---> Salir')
    print('Bye Bye')            
        


        
        
print('gracias ', nombre,'\n\n')
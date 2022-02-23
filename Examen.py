### Luis Fernando Puch Acantar  13000919

clave=open("C:/Users/luisp/Documents/HERRAMIENTAS 2/clave.txt","r")
b=[]
for i in clave:
    a=i.split() ##Filas 
    b.append(a) 

num=b[0]
let=b[1]

def encriptar(texto,num):
    c=len(texto) 
    conversion=[]
    for i in range (0,c): 
        for j in range(0,len(let)): 
            if texto[i]==let[j]:
                conversion.append(num[j])
    print("\n")
    print("Texto encriptado")
    print(*conversion)
    return

def desencriptar(texto,let):
    c=len(texto) 
    conversion=[]
    for i in range (0,c): 
        for j in range(0,len(num)): 
            if texto[i]==num[j]:
                conversion.append(let[j])
    print("\n")
    print("Texto desencriptado")
    print(*conversion)
    print("\n")
    return


def menu():
    """Función que muestra el menu """ 
    print("\n")   
    print ("Menu")
    print ("1- Encripta")
    print ("2- Desencripta")
    print ("3- Salir")
    print("\n")

while True:
    
    menu()
    opcionMenu = int(input("Selecciona una opcion:    "))
    print("\n")
    if opcionMenu==1:
        texto=input("Dime el texto: " ) 
        encriptar(texto,num)
    elif opcionMenu==2:
        texto1=input("Dime el texto: " ) 
        texto=texto1.split()
        desencriptar(texto,let)
    elif opcionMenu==3:
        break
    else:
        print ("")
        input("No has pulsado ninguna opción correcta.Pulsa enter para continuar")
clave.close()



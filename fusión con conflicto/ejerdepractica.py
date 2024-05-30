print("Bienvenido al menú de cálculo")
def mostrarmenu():

    print("e) Salir")
    
mostrarmenu()
opc=input("Seleccione una opción...")

while opc!="e":

    if opc=="a":
        lado=int(input("ingresar el lado : "))
        while lado<0:
            lado=int(input("ingresar un lado nuevamente"))

        area= lado**2 
        perimetro= lado + lado + lado + lado 

        print(f"el area del cuadrado es: {area} y el perimetro es: {perimetro}")

    if opc=="b":
        base= int(input("ingrese la base: "))
        while base<0:
            base= int(input("ingrese la base con valor positivo: "))
        altura=int(input("ingrese la altura: "))
        while altura<0:
            altura=int(input("ingrese la altura con valor positivo: "))

        area= base * altura 
        perimetro =  base*2 + altura*2 

        print(f"el area del rectangulo es: {area} y el perimetro es: {perimetro}")

    if opc=="c":
        lado1=int(input("ingresar lado del triangulo"))
        lado2=int(input("ingresar lado del triangulo"))
        lado3=int(input("ingresar lado del triangulo"))

        while lado1<0 or lado2<0 or lado3<0 : 
            if lado1<0:
                lado1=int(input("ingresar lado del triangulo"))
            if lado2<0:
                lado2=int(input("ingresar lado del triangulo"))
            if lado3<0:
                lado3=int(input("ingresar lado del triangulo"))
        
        perimetro= lado1+ lado2 + lado3
        s= perimetro/2
        area= (s(s-lado1)*(s-lado2)*(s-lado3))**0.5

        print(f"el area del triangulo es: {area} y el perimetro es: {perimetro}")
        
    if opc=="d":
        radio= int(input("ingrese el radio: "))
        while radio<0: 
            radio= int(input("ingrese el radio con valor positivo: "))
        
        area= 3.14 * radio**2
        perimetro= 2 * 3.14 * radio

        print(f"el area del circulo es: {area} y el perimetro es: {perimetro}")

    
    mostrarmenu()
    opc=input("Seleccione una opción...")

    

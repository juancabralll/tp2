palabra=input("ingresar una palabra  \n")

vocal=0
consonante=0 

for i in palabra:
    if i  in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
        vocal+=1
    else:
        consonante+=1
    
print("VOCALES ", vocal)
print("consonantes ",consonante)
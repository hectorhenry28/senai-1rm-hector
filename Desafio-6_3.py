nota1 = float( input("informe nota1") )
nota2 = float( input("informe nota2") ) 
nota3 = float( input("informe nota3") )

media = (nota1 + nota2 + nota3)/3 

if media >= 6:
    print("Aprovado")
else:
    if media >= 5:
       print ("Conselho de classe") 
    else:
        print("Reprovado")

    print("A media foi " , media)


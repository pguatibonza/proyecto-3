palabra="v"
letras_repeticiones={}
repeticiones_palabra={}
letras_inversas=""
i=len(palabra)-1

#Inserta en una tabla de hash las letras de toda la cadena y cuantas veces se repiten en esta
def repeticiones_letras(palabra):
    letras_repeticiones={}
    for letra in palabra:
        if letra not in letras_repeticiones:
            letras_repeticiones[letra]=0
        letras_repeticiones[letra]+=1
    return letras_repeticiones

letras_repeticiones=repeticiones_letras(palabra)

cantidad_letras=len(letras_repeticiones)
contador=cantidad_letras
ubicacion=i
while i>=0 :
    if palabra[i] not in letras_inversas:
        letras_inversas+=palabra[i]
        repeticiones_palabra[palabra[i]]=int(letras_repeticiones[palabra[i]]/contador)
        contador-=1
        i=ubicacion
        for letra in letras_inversas:
            i-=repeticiones_palabra[letra]
        ubicacion=i
    else:
        i-=1


#busca cuantas repeticiones de cada letra hay en una sola palabra
def getPalabra_inicial(repeticiones_palabra):
    tamanio_palabra=0
    for letra in repeticiones_palabra:
        tamanio_palabra+=repeticiones_palabra[letra]

    return palabra[:tamanio_palabra]

palabra_inicial=getPalabra_inicial(repeticiones_palabra)

def invertir_letras(letras_inversas):
    letras=""
    j=len(letras_inversas)-1
    while j>=0:
        letras+=letras_inversas[j]
        j-=1
    return letras


letras=invertir_letras(letras_inversas)



def verificacion_palabra(letras,palabra_inicial,cadena_inicial):
    palabra=palabra_inicial

    for letra in letras:
        cadena=""
        for letra_2 in palabra_inicial:
            if letra_2!=letra:
                palabra+=letra_2
                cadena+=letra_2
        palabra_inicial=cadena
   
    return cadena_inicial==palabra

        
if verificacion_palabra(letras,palabra_inicial,palabra) :
    print(palabra_inicial + " " + letras)
else: 
    print("no existe")


        
            






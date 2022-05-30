from time import process_time

def desencriptacion(palabra):
    letras_repeticiones={}
    letras_repeticiones=repeticiones_letras(palabra)
    letras_inversas=""
    repeticiones_palabra={}
    i=len(palabra)-1
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

    palabra_inicial=getPalabra_inicial(repeticiones_palabra,palabra)
    letras=invertir_letras(letras_inversas)

    if verificacion_palabra(letras,palabra_inicial,palabra) :
        return palabra_inicial + " " + letras+"\n"
    else: 
        return "NO EXISTE\n"

#Inserta en una tabla de hash las letras de toda la cadena y cuantas veces se repiten en esta
def repeticiones_letras(palabra):
    letras_repeticiones={}
    for letra in palabra:
        if letra not in letras_repeticiones:
            letras_repeticiones[letra]=0
        letras_repeticiones[letra]+=1
    return letras_repeticiones







#busca cuantas repeticiones de cada letra hay en una sola palabra
def getPalabra_inicial(repeticiones_palabra,palabra):
    tamanio_palabra=0
    for letra in repeticiones_palabra:
        tamanio_palabra+=repeticiones_palabra[letra]

    return palabra[:tamanio_palabra]



def invertir_letras(letras_inversas):
    letras=""
    j=len(letras_inversas)-1
    while j>=0:
        letras+=letras_inversas[j]
        j-=1
    return letras






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

archivo=open("in.in","r")
salida=open("out.out","w")
cantidad=int(archivo.readline())

t1_start = process_time() 
while (cantidad>0):
    
    palabra=archivo.readline()
    palabra=palabra.replace("\n","")
    cadena=desencriptacion(palabra)
    salida.write(cadena)
    cantidad-=1

t1_stop = process_time()
salida.write(str(t1_stop-t1_start))         






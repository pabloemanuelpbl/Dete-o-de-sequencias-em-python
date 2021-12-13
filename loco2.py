def encontrar(num):
    ## gera um arrei na variavel lista    
    lista = []
    entrada = str(num)
    for i in entrada:
        lista += i

    numList = len(lista)            #exemplo: 5
    res = {}                        #resposta 
    ii = 0
    espaco = 1
    for i in range((numList-1)):    #ficaria 4
        agora = int(lista[i+1])     
        atras = int(lista[i])
        if(agora-1 == atras):       #se o valor de agora - 1 é igual a o valor de atras
            if(espaco==0):
                res[ii+1]=-2
                ii+=2
                espaco=1
            res[ii] = atras
            res[ii+1] = agora
        elif(agora==0 and atras==9):
            if(espaco==0):
                res[ii+1]=-2
                ii+=2
                espaco=1
            res[ii]=9
            res[ii+1]=0
        else:
            espaco = 0
        ii += 1
    #print(res) #se quiser debugar
        
    resFim = ""
    antes = 0
    resf = ''
    for i in res.values():
        if(antes+1==i or (antes==9 and i==0)):
            resf+=str(i)
        else:  
            if (len(resf)>len(resFim)):
                resFim=resf
            resf = str(i)
            if(resf=='-2'):
                resf=''
        antes = i
    if (len(resf)>len(resFim)):
        resFim=resf
    
    print(resFim) # omita esta linha se nao quiser ver
    return resFim   # return é útil para utilizar com outros códigos


##  exemplo
#   executar no shell
digite = int(input('digite numeros inteiros: '))
encontrar(digite)
import json
g = open('JobRotation/Código Python/dados.json')
dados = json.load(g)
 
 aux = 0
 maior = 0
 menor = 0
 soma = 0
 media = 0
 for dia in dados:
    
    
    if (dia['valor']) != 0:
        aux = dia['valor']

        
        if (aux > maior):
            maior = aux

        
        if(menor == 0):
            menor = aux
        elif (aux < menor):
            menor = aux

        
        soma += dia['valor']
        
        print('O maior valor de faturamento do mês R$ ' + str(maior))
        print('O menor valor de faturamento do mês R$ ' + str(menor))
        
        media = soma / len(dados)
        faturamento = ''
        
        for i in dados:
            if (i['valor']) != 0:
        
                if (i['valor']) > media:
                    faturamento += (str(i['dia']) + ' ')
        
                    print('Os dias em que o faturamento foi maior que a média mensal foram: ' + faturamento)
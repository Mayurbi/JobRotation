sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

valorTotal = sp + mg + rj + es + outros

def porc (estado, valorTotal):
    return round(((100*estado)/valorTotal),2)
print("Valor Mensal de São Paulo:" + str(porc(sp, valorTotal)) + '%')
print("Valor Mensal do Rio de Janeiro:" + str(porc(rj, valorTotal)) + '%')
print("Valor Mensal de Minas Gerais:" + str(porc(mg, valorTotal)) + '%')
print("Valor Mensal de Espírito Santo:" + str(porc(es, valorTotal)) + '%')
print("Valor Mensal de Outros:" + str(porc(outros, valorTotal)) + '%')
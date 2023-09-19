#url para pesquisar
url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

#Sanitização da url
url = url.lower().strip()

# Validação da URL
if url == "":
    raise ValueError("A url está vazia")

#separando urls
indice_interrogacao = url.find('?')
tamanho_url = len(url)
url_base = url[0:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:tamanho_url+1]
# print(url_parametros)

# achando parametros
# primeiro parametro acha a partir do ? ate o igual,  resto vai do & ate o igual
# indice_do_igual3 = url_parametros.find("=")
# indice_do_igual2 = url_parametros.rfind("=")
# indice_do_divisor = url_parametros.find('&', indice_do_igual)
# lista_de_parametros = [url_parametros[:indice_do_igual], url_parametros[indice_do_divisor+1:indice_do_igual2]]
# # print(lista_de_parametros)

igual = "="
indice = 0
lista_dos_iguais = []
for i in range(len(url_parametros)):
    indices_do_igual = url_parametros.find(igual,indice)
    if (indices_do_igual != -1):
        lista_dos_iguais.append(indices_do_igual)
        indice = indices_do_igual + 1

print(lista_dos_iguais)

lista_de_parametros = []
start_for = 0
for i in lista_dos_iguais:
    indice_do_divisor = url_parametros.find("&", start_for, i)
    start_for = indice_do_divisor+1
    print(indice_do_divisor)
    if indice_do_divisor == -1:
        lista_de_parametros.append(url_parametros[:i])
    else:
        lista_de_parametros.append(url_parametros[indice_do_divisor+1:i])


print(lista_de_parametros)

# achando paramentros
print(url_parametros)
nome_do_paramentro = "quantidade"
achar_parametro = url_parametros.find(nome_do_paramentro)
tamanho_do_parametro = len(nome_do_paramentro)
indice_do_parametro = achar_parametro + tamanho_do_parametro + 1
achar_divisor = url_parametros.find('&',achar_parametro)
print(achar_divisor)

parametro_com_divisor = url_parametros[indice_do_parametro:achar_divisor]

if achar_divisor == -1:
    valor = url_parametros[indice_do_parametro:]
else:
    valor = url_parametros[indice_do_parametro:achar_divisor]

print(valor)

# print(url_parametros)
# parametro_busca = 'moedaOrigem'
# indice_parametro = url_parametros.find(parametro_busca)
# print(indice_parametro)
#
# indice_valor = indice_parametro + len(parametro_busca) + 1
# print(indice_valor)
#
# indice_e_comercial = url_parametros.find('&', indice_valor)
# print(indice_e_comercial)
#
# if indice_e_comercial == -1:
#     valor = url_parametros[indice_valor:]
# else:
#     valor = url_parametros[indice_valor:indice_e_comercial]
# print(valor)

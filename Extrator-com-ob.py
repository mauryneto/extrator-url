
import re


class ExtratorUrl:

    def __init__(self, url):
        self.parametro = None
        self.url = self.sanitizar_url(url)
        self.validar_url()

    @staticmethod
    def sanitizar_url(url):
        if type(url) == str:
            return url.strip().lower()
        else:
            return ""

    def validar_url(self):
        if not self.url:
            raise ValueError("A url está vazia")
        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)
        if not match:
            print("A url não é valida")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[0:indice_interrogacao]
        return url_base

    def get_url_parametro(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_nome_parametro(self):
        igual = "="
        indice = 0
        lista_dos_iguais = []
        for i in range(len(self.get_url_parametro())):
            indices_do_igual = self.get_url_parametro().find(igual, indice)
            if indices_do_igual != -1:
                lista_dos_iguais.append(indices_do_igual)
                indice = indices_do_igual + 1

        lista_de_parametros = []
        start_for = 0
        for i in lista_dos_iguais:
            indice_do_divisor = self.get_url_parametro().find("&", start_for, i)
            start_for = indice_do_divisor + 1
            if indice_do_divisor == -1:
                lista_de_parametros.append(self.get_url_parametro()[:i])
            else:
                lista_de_parametros.append(self.get_url_parametro()[indice_do_divisor + 1:i])
        return ', '.join(lista_de_parametros)

    def get_valor_parametro(self, parametro):
        self.parametro = parametro.lower()
        achar_parametro = self.get_url_parametro().find(parametro)
        tamanho_do_parametro = len(parametro)
        indice_do_parametro = achar_parametro + tamanho_do_parametro + 1
        achar_divisor = self.get_url_parametro().find('&', achar_parametro)

        if achar_divisor == -1:
            valor = self.get_url_parametro()[indice_do_parametro:]
        else:
            valor = self.get_url_parametro()[indice_do_parametro:achar_divisor]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return "URL: " + self.url + "\n" + "Parametros: " + self.get_nome_parametro()

    def __eq__(self, other):
        return self.url == other.url

    def conversao(self):
        valor_dolar = float(5.5)
        valor_real = 1
        conversao = valor_dolar*valor_real*float(self.get_valor_parametro("quantidade"))
        return conversao


url_escrita = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorUrl(url_escrita)
print(extrator_url)

moeda_origem = extrator_url.get_valor_parametro("moedaorigem")
moeda_destino = extrator_url.get_valor_parametro("moedadestino")
quantidade = extrator_url.get_valor_parametro("quantidade")
valor_convertido = extrator_url.conversao()
print(f'\nConvertendo:')
print(f'Moeda de origem: {moeda_destino}\nMoeda de destino: {moeda_destino}\nQuantidade: {quantidade}')
print(f'Valor da conversão: {valor_convertido}')

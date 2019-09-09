#!python3

# http://www.isbn.bn.br/website/tabela-de-idiomas?d-444655-p=1
# Páginas de 1 a 17

import requests, csv
from bs4 import BeautifulSoup


def main():
	lista_idiomas = []

	for i in range(1, 18):
		url = 'http://www.isbn.bn.br/website/tabela-de-idiomas?d-444655-p={}'.format(i)
		html = get_html(url)
		resultados_pagina = web_scrap(html)
		for resultado in resultados_pagina:
			lista_idiomas.append(resultado)

	create_csv(lista_idiomas)

def get_html(url):
	try:
		html = requests.get(url)
		return html.text
	except:
		raise Exception('Não foi possível pegar o HTML da página')

def web_scrap(html_text):
	soup = BeautifulSoup(html_text, 'html.parser')
	resultado = []
	
	tabela = soup.find(id='idioma')
	tbody = tabela.find('tbody')
	linhas = tbody.find_all('tr')

	for linha in linhas:
		sigla = linha.find_all('td')
		sigla_descricao = [sigla[0].get_text().upper(), sigla[1].get_text().upper()]
		resultado.append(sigla_descricao)

	return resultado

def create_csv(dados):
	csv_data = dados

	with open('idiomas.csv', 'w') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerows(csv_data)
	csv_file.close()


if __name__ == '__main__':
	main()


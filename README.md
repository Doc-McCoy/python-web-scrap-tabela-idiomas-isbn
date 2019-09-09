# Web Scrap para coletar Sigla - Idiomas de uma tabela.

### O que é
Web Scrap que acessa o site da [Agência Brasileira do ISBN](http://www.isbn.bn.br/website/tabela-de-idiomas?d-444655-p=1), na sessão das tabelas de Idiomas, e varre todas as **17 páginas** da tabela coletando a **Sigla** e a **Descrição** dos idiomas.

Este script cria um arquivo CSV com os dados da tabela.

### Como usar:

#### 1. Criar e ativar o ambiente virtual
```bash
$python -m venv venv
$source venv/bin/activate
```

#### 2. Instalar os requerimentos
```bash
$pip install -r requirements.txt
```

#### 3. Executar
```bash
$python idiomas-scrap.py
```

*Feito às pressas rapidinho, mas funciona que é uma beleza :)*

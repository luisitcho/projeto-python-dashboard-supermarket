# Projeto Python: Dashboard Supermarket

Dashboard sobre uma grande rede de varejo, com o objetivo de mostrar:

* Com uma visão mensal
* Faturamento por unidade
* Tipo de produto mais vendido
* Contribuição por filial
* Desempenho das forma de pagamento
* Como estão as avaliações das filiais

## Comandos necessários

### 1. Crie o ambiente virtual
```
. venv/bin/activate
```

### 2. Instale o `pip-tools`
```
pip install pip-tools
```

### 3. Criação do arquivo `requirements.in`
Este arquivo deve listar todas as dependências do seu projeto, normalmente de forma simples. Exemplo de conteúdo do `requirements.in`:
```
streamlit
pandas
matplotlib
```

### 4. Gerar o `requirements.txt`
O comando `pip-compile` vai compilar o arquivo `requirements.txt` a partir do `requirements.in`, resolvendo todas as dependências (incluindo as versões).
```
pip-compile requirements.in --output-file requirements.txt
```
Isso vai gerar o `requirements.txt` com as versões exatas das dependências.

### 5. Instalar as dependências
O comando `pip install -r requirements.txt` instala as dependências listadas no `requirements.txt`:
```
pip install -r requirements.txt
```

### 6. Iniciar a aplicação com Streamlit
Para rodar sua aplicação Streamlit, use:
```
streamlit run dashboards.py
```
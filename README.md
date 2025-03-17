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
O comando pip install -r requirements.txt instala as dependências listadas no `requirements.txt`:
```
pip install -r requirements.txt
```

### 5. Execute comando abaixo no terminal para iniciar a aplicação:
```
 streamlit run dashboards.py
```
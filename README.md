# Análise Demográfica com Pandas

Este projeto, feito no curso Data Analysis with Python da plataforma freeCodeCamp, analisa dados demográficos a partir do conjunto de dados `adult.data.csv`. Utilizando a biblioteca Pandas, ele extrai informações estatísticas sobre educação, salários, etnias e outros aspectos.

## Funcionalidades
- Contagem de pessoas por etnia.
- Cálculo da idade média dos homens.
- Percentual de pessoas com graduação (Bacharelado).
- Comparativo de salário para pessoas com e sem educação avançada.
- Cálculo do número mínimo de horas trabalhadas por semana.
- Identificação do país com maior percentual de pessoas que ganham mais de 50K.
- Profissão mais comum entre os indianos que ganham mais de 50K.

## Requisitos
- Python 3.x
- Pandas

Instale os requisitos com:
```bash
pip install pandas
```

## Como Usar
1. Baixe o arquivo `adult.data.csv` e coloque-o no mesmo diretório do script.
2. Execute o script Python:
```bash
python demographic_data_analyzer.py
```
3. O resultado será retornado em formato de dicionário com os valores calculados.

## Estrutura do Projeto
```
|-- adult.data.csv  # Conjunto de dados
|-- demographic_data_analyzer.py       # Código-fonte principal
|-- README.md       # Documentação do projeto
```


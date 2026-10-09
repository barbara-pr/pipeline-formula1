# 🏎️ Formula 1 Data Pipeline

Pipeline de dados desenvolvido para estudar e praticar conceitos de **Engenharia de Dados**, utilizando dados históricos do Campeonato Mundial de Fórmula 1.

## 🎯 Objetivo

Investigar a relação entre a **posição de largada** e a **posição final** dos pilotos de Fórmula 1.

A pergunta principal da análise é:

> **Qualificação realmente importa?**

A partir dos resultados históricos, o projeto busca entender se pilotos que largam em posições melhores tendem a terminar melhor colocados e quantas posições os pilotos costumam ganhar ou perder durante uma corrida.

Um dos casos de interesse é o **GP de Mônaco de 2018**, com destaque para a corrida de **Max Verstappen**, que largou na **P20 e terminou na P9**. O resultado chama atenção especialmente por se tratar de um circuito conhecido pela dificuldade de ultrapassagem, tornando a recuperação de posições ao longo da corrida um aspecto interessante para análise.


## 📊 Dados

Os dados utilizados são provenientes do dataset:

**Formula 1 World Championship 1950–2020**

O dataset contém diferentes arquivos relacionados ao campeonato, incluindo:

* `qualifying.csv` — dados de qualificação;
* `results.csv` — resultados das corridas;
* `races.csv` — informações sobre as corridas;
* `drivers.csv` — informações sobre os pilotos;
* `constructors.csv` — informações sobre as equipes/construtores.

## 🔄 Pipeline

O projeto será construído seguindo um fluxo ETL:

```text
Kaggle
   ↓
Arquivos CSV
   ↓
Extract
   ↓
Transform
   ↓
Load
   ↓
PostgreSQL
   ↓
Análise
```

### Extract

Leitura dos arquivos CSV utilizando Python.

### Transform

Limpeza, seleção e combinação dos dados necessários para responder às perguntas da análise.

A ideia é chegar a uma estrutura semelhante a:

| Ano  | Corrida | Piloto | Posição de largada | Posição final |
| ---- | ------- | ------ | -----------------: | ------------: |
| 2018 | Monaco  | ...    |                ... |           ... |

### Load

Os dados transformados serão armazenados em um banco **PostgreSQL**.

## 🛠️ Tecnologias

* Python
* Pandas
* PostgreSQL
* SQL
* Docker
* Git / GitHub

## 📈 Análises planejadas

* Relação entre posição de largada e posição final;
* Ganho e perda de posições durante as corridas;
* Influência da posição de largada no resultado final;
* Análise do GP de Mônaco de 2015;

## 📁 Estrutura do projeto

```text
formula-1-data-pipeline/
│
├── data/
│   └── ...
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── main.py
├── docker-compose.yml
└── README.md
```

## 📚 Objetivo de aprendizado

Este projeto está sendo desenvolvido como uma prática pessoal de **Data Engineering**, com foco em compreender na prática:

* ETL;
* manipulação de dados com Python/Pandas;
* relacionamento entre diferentes datasets;
* bancos de dados relacionais;
* PostgreSQL;
* Docker e containers;
* organização de projetos de dados;

---

### 👩‍💻 Projeto

Desenvolvido por **Bárbara Pereira Raposo** como projeto de estudo em Engenharia de Dados.

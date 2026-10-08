import pandas as pd
from sqlalchemy import create_engine


def load_data(dados):

    # 1. CRIAR CONEXÃO COM O POSTGRESQL
    engine = create_engine(
        "postgresql://postgres:postgres@localhost:5432/f1"
    )

    # 2. ENVIAR OS DADOS PARA O BANCO
    dados.to_sql(
        "f1_results",
        engine,
        if_exists="replace",
        index=False
    )

    print("Dados carregados com sucesso no PostgreSQL!")
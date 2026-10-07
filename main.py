from src.extract import extract
from src.transform import transform_data


def pipeline():
    print("=== INICIANDO PIPELINE ===")

    # 1. EXTRACT
    print("\n[1/2] Extraindo dados...")

    qualifying, results, races, drivers, constructors = extract()

    print("Extract concluído!")
    print(f"Qualifying: {len(qualifying)} registros")
    print(f"Results: {len(results)} registros")
    print(f"Races: {len(races)} registros")
    print(f"Drivers: {len(drivers)} registros")
    print(f"Constructors: {len(constructors)} registros")

    # 2. TRANSFORM
    print("\n[2/2] Transformando dados...")

    dados = transform_data(
        qualifying,
        results,
        races,
        drivers,
        constructors
    )

    print("Transform concluído!")
    print(f"Dados finais: {len(dados)} registros")

    dados.to_csv("data/dados_transformados.csv", index=False)

    print("Dados transformados salvos!")

    return dados


if __name__ == "__main__":
    pipeline()
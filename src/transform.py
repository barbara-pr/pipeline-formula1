import pandas as pd

def transform_data(qualifying, results, races, drivers, constructors):

    # 1. PREPARAR QUALIFYING

    qualifying = qualifying.rename(
        columns={
            "position": "qualifying_position"
        }
    )

    qualifying = qualifying[
        [
            "raceId",
            "driverId",
            "constructorId",
            "qualifying_position"
        ]
    ]

    # 2. PREPARAR RESULTS

    results = results.rename(
        columns={
            "positionOrder": "final_position",
            "grid": "grid_position"
        }
    )

    results = results[
        [
            "raceId",
            "driverId",
            "constructorId",
            "grid_position",
            "final_position",
            "points",
            "statusId"
        ]
    ]

    # 3. JUNTAR QUALIFYING + RESULTS

    dados = qualifying.merge(
        results,
        on=["raceId", "driverId", "constructorId"],
        how="inner"
    )

    # 4. PREPARAR RACES

    races = races.rename(
        columns={
            "name": "race"
        }
    )

    races = races[
        [
            "raceId",
            "year",
            "race"
        ]
    ]

    # 5. JUNTAR INFORMAÇÕES DA CORRIDA

    dados = dados.merge(
        races,
        on="raceId",
        how="left"
    )

    # 6. PREPARAR DRIVERS

    drivers["driver"] = (
        drivers["forename"] + " " + drivers["surname"]
    )

    drivers = drivers[
        [
            "driverId",
            "driver"
        ]
    ]

    # 7. JUNTAR NOME DO PILOTO

    dados = dados.merge(
        drivers,
        on="driverId",
        how="left"
    )

    # 8. PREPARAR CONSTRUCTORS

    constructors = constructors.rename(
        columns={
            "name": "constructor"
        }
    )

    constructors = constructors[
        [
            "constructorId",
            "constructor"
        ]
    ]

    # 9. JUNTAR NOME DA EQUIPE

    dados = dados.merge(
        constructors,
        on="constructorId",
        how="left"
    )

    # 10. ORGANIZAR AS COLUNAS

    dados = dados[
        [
            "year",
            "race",
            "driver",
            "constructor",
            "qualifying_position",
            "grid_position",
            "final_position",
            "points",
            "statusId"
        ]
    ]

    return dados 
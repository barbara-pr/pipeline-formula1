import pandas as pd

def extract():
    qualifying = pd.read_csv("data/qualifying.csv")
    results = pd.read_csv("data/results.csv")
    races = pd.read_csv("data/races.csv")
    drivers = pd.read_csv("data/drivers.csv")
    constructors = pd.read_csv("data/constructors.csv")

    return qualifying, results, races, drivers, constructors

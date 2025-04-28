import pandas as pd

def load_data():
    df = pd.read_csv("data/titanic.csv")
    return df[df['sex'] == 'male']
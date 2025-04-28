import pandas as pd

def load_data():
    df = pd.read_csv("data/titanic.csv")
    return df[df['sex'] == 'male']


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the input DataFrame by:
    - Dropping rows with missing values
    - Converting all categorical columns to lowercase

    Parameters:
    df (pd.DataFrame): The input DataFrame to clean.

    Returns:
    pd.DataFrame: The cleaned DataFrame.
    
    Example:
    >>> import pandas as pd
    >>> df = pd.DataFrame({'Name': ['Alice', None, 'Bob'], 'City': ['New York', 'Berlin', 'Paris']})
    >>> clean_data(df)
        Name     City
    0  alice  new york
    2    bob     paris
    """
    df = df.dropna()
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.lower()
    return df

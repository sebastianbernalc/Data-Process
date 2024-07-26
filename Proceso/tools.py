
import numpy as np


def remove_negative_values(df, column):
    '''
    This function removes negative values from a column in a DataFrame by replacing them with NaN.
    
    Parameters:
        df: DataFrame
        column: str
        
    Returns:
        DataFrame
    '''
    df[column] = df[column].apply(lambda x: np.nan if x < 0 else x)
    return df

def remove_outliers(df, column, threshold = 2):
    '''
    This function removes outliers from a column in a DataFrame by replacing them with the mean of the column.
    The threshold parameter is used to determine the minimum z-score that a value must have in order to be considered an outlier.

    Parameters:
        df: DataFrame
        column: str
        threshold: int or float

    Returns:
        DataFrame
    '''
    column_mean = df[column].mean()
    column_std = df[column].std()
    df[column] = df[column].mask(((df[column] - column_mean) / column_std).abs() > threshold, column_mean)
    return df

def map_column_values(df, column, dict):
    ''' This function maps the values of a column in a DataFrame to new values based on a dictionary.
        if the value is not in the dictionary, it is replaced with NaN.
        
        Parameters:
            df: DataFrame
            column: str
            dict: dict
        
        Returns:
            DataFrame'''
    
    df[column] = df[column].apply(lambda value: dict.get(value, value))
    return df

def fill_na_value(df, column, value):
    ''' This function fills the NaN values in a column of a DataFrame with a specified value.
        
        Parameters:
            df: DataFrame
            column: str
            value: int, float, str
        
        Returns:
            DataFrame'''
    df[column].fillna(value, inplace=True)
    return df
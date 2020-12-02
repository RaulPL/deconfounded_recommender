"""
Load data
"""

import pandas as pd


def load_ratings(path) -> pd.DataFrame:
    names = ['userId', 'movieId', 'rating', 'timestamp']
    df = pd.read_csv(path, sep='\t', names=names)
    return df

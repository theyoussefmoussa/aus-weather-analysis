import numpy as np


def diff(df, col_a, col_b, new_col):
    df[new_col] = df[col_a] - df[col_b]
    return df


def average(df, col_a, col_b, new_col):
    df[new_col] = (df[col_a] + df[col_b]) / 2
    return df


def interaction(df, col_a, col_b, new_col):
    df[new_col] = df[col_a] * df[col_b]
    return df


def log_transform(df, col, new_col):
    df[new_col] = np.log1p(df[col])
    return df
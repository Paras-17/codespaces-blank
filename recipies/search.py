import csv
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import sys
import matplotlib.pyplot as plt
import seaborn as snsle
import dask as dd

df = pd.read_csv("recipies/RAW_recipes.csv")

def raw_recipes(df):
    ingredients = input("Enter ingredients: ").split(',')
    results = []
    for index, row in df.iterrows():
        count = 0
        for ingredient in ingredients:
            if ingredient in str(row.values):
                count += 1
        if count == len(ingredients):
            results.append(row.values)
            
    if results:
        results_df = pd.DataFrame(results, columns=df.columns)
        print(results_df)
    else:
        print("No results found")

raw_recipes(df)

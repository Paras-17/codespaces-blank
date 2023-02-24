import csv
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import sys
import matplotlib.pyplot as plt
import seaborn as snsle
results = []


df = pd.read_csv("E:\\project\\recipies\\RAW_recipes.csv")

def raw_recipes(df, ingredients):
    
    for index, row in df.iterrows():
        count = 0
        for ingredient in ingredients:
            if ingredient in str(row.values):
                count += 1
        if count == len(ingredients):
            results.append(row.values)
            
    #for result in results:
        #print(result)

ingredients = ['pineapple','chicken','lemon','onion','egg']
raw_recipes(df, ingredients)


for result in results:
        print(result)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import argparse
from pathlib import Path
import os

def impute_data(column, missing_values):
  mean = column.mean()
  sigma = column.std()
  generated_data = np.random.normal(mean, sigma, missing_values)
  column[column.isna()] = generated_data

parser = argparse.ArgumentParser("score")
parser.add_argument("--data_set", type=str, help="Path to the dataset")
parser.add_argument("--data_clean_output", type=str, help="Path of the clean dataset")
parser.add_argument("--pair_plot_folder", type=str, help="Path of the pair plot folder")

args = parser.parse_args()

print("Hola desde Clean data...")

lines = [
    f"Data set: {args.data_set}",
    f"Data clean output: {args.data_clean_output}",
    f"Corr matrix output: {args.pair_plot_folder}",
]

print("Parametros: ...")

for line in lines:
    print(line)

water_potability_df = pd.read_csv(args.data_set)
nulls_serie = water_potability_df.isnull().sum()

impute_data(water_potability_df['ph'], nulls_serie['ph'])
impute_data(water_potability_df['Sulfate'], nulls_serie['Sulfate'])
impute_data(water_potability_df['Trihalomethanes'], nulls_serie['Trihalomethanes'])

# Create a pair plot
filename = 'pair_plot.jpg'
sns.set(style="ticks")
sns.pairplot(water_potability_df, diag_kind='kde')
plt.suptitle("Pair Plot of Columns")
plt.savefig(open((Path(args.pair_plot_folder) / filename), "wb"))

water_potability_df.to_csv(args.data_clean_output)
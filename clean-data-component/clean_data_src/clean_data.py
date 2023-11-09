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
parser.add_argument("--corr_matrix_output", type=str, help="Path of the correlation matrix")

args = parser.parse_args()

print("Hola desde Clean data...")

lines = [
    f"Data set: {args.data_set}",
    f"Data clean output: {args.data_clean_output}",
    f"Corr matrix output: {args.corr_matrix_output}",
]

print("Parametros: ...")

for line in lines:
    print(line)

water_potability_df = pd.read_csv(Path(args.data_set))
nulls_serie = water_potability_df.isnull().sum()

impute_data(water_potability_df['ph'], nulls_serie['ph'])
impute_data(water_potability_df['Sulfate'], nulls_serie['Sulfate'])
impute_data(water_potability_df['Trihalomethanes'], nulls_serie['Trihalomethanes'])

correlation_matrix = water_potability_df.corr(method='pearson')

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, vmin=-1, vmax=1)
plt.title('Correlation Heatmap')
#plt.savefig(f'{args.corr_matrix_output}.jpg',bbox_inches='tight',dpi=100)

water_potability_df.to_csv(f'{args.data_clean_output}.csv')
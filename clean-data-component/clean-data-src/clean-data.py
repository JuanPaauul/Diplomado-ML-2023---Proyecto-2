import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import argparse

def impute_data(column, missing_values):
  mean = column.mean()
  sigma = column.std()
  generated_data = np.random.normal(mean, sigma, missing_values)
  column[column.isna()] = generated_data

parser = argparse.ArgumentParser("score")
parser.add_argument("--data_set", type=str, help="Path to the dataset")

args = parser.parse_args()

water_potability_df = pd.read_csv(args.data_set)
nulls_serie = water_potability_df.isnull().sum()

impute_data(water_potability_df['ph'], nulls_serie['ph'])
impute_data(water_potability_df['Sulfate'], nulls_serie['Sulfate'])
impute_data(water_potability_df['Trihalomethanes'], nulls_serie['Trihalomethanes'])

correlation_matrix = water_potability_df.corr(method='pearson')

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, vmin=-1, vmax=1)
plt.title('Correlation Heatmap')
plt.savefig('corr_matrix.png',bbox_inches='tight',dpi=100) # TODO set the appropriate path to save.

water_potability_df.to_csv('../../water-potability-clean.csv') # TODO set the appropriate path to save.
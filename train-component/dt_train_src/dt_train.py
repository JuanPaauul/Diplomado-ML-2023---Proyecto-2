import argparse
from pathlib import Path
from uuid import uuid4
from datetime import datetime
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import pickle

# obtener parámetros:
parser = argparse.ArgumentParser("dt_train")
parser.add_argument("--training_data", type=str, help="Path to training data")
parser.add_argument("--criterion", type=str, help="The function to measure the quality of a split")
parser.add_argument("--min_samples_split", type=int, help="The minimum number of samples required to split an internal node")
parser.add_argument("--max_depth", type=int, help="The maximum depth of the tree")
parser.add_argument("--model_output", type=str, help="Path of output model")

args = parser.parse_args()

print("Hola desde DT_train...")

lines = [
    f"Training data path: {args.training_data}",
    f"Criterion: {args.criterion}",
    f"Min samples Split: {args.min_samples_split}",
    f"Max depth: {args.max_depth}",
    f"Model output path: {args.model_output}",
]

print("Parametros: ...")

# imprimir parámetros:

for line in lines:
    print(line)

# Leemos el dataset desde clean_data
training_data = pd.read_csv(args.training_data)

# Dependent vs Independent Variables
X_train = training_data.drop(columns=['Potability'])
y_train = training_data['Potability']

# Se realiza el entrenamiento del modelo
dt = DecisionTreeClassifier(criterion= args.criterion, min_samples_split= args.min_samples_split, max_depth=args.max_depth)
dt.fit(X_train,y_train)
# Imprimimos las variables independientes que influencuiaran a la toma de decisiones del modelo 
print(X_train.columns.to_list())
# Guardamos el graficos de el arbol de deciciones que se armo en base al moelo entrenado
fig = plt.figure(figsize=(25,20))
_ = tree.plot_tree(dt, 
                   feature_names=X_train.columns.to_list(),  
                   class_names=['Not Potable', 'Potable'],
                   filled=True)
# Guardamos esa imagen en un archivo .svg que facilita su visiualizacion en entornos web
fig.savefig(f'{args.model_output}/water-decision-tree.svg')

# Guardar el modelo creado 
filename = f'{args.model_output}/decission_tree_modelo.pkl'
pickle.dump(dt, open(filename, "wb"))
#pickle.dump(dt, open(args.model_output, "wb"))
print(f"modelo guardado en {args.model_output}")


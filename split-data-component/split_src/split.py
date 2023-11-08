import argparse
from pathlib import Path
from uuid import uuid4
from datetime import datetime
import os

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import pandas as pd
import pickle

# obtener parámetros:
parser = argparse.ArgumentParser("split")
parser.add_argument("--clean_data", type=str, help="Path to a clean dataset")
parser.add_argument("--split_ratio_train", type=float, help="Split ratio given for training")
parser.add_argument("--data_train", type=str, help="Training dataset file")
parser.add_argument("--data_test", type=str, help="Testing dataset file")

args = parser.parse_args()

print("Hola desde split...")

lines = [
    f"clean_data: {args.clean_data}",
    f"split_ratio for training: {args.split_ratio_train}",
    f"data_train: {args.data_train}",
    f"data_test: {args.data_test}",
]

print("Parametros: ...")

# imprimir parámetros:

for line in lines:
    print(line)
# Leemos el dataset desde clean_data
clean_data = pd.read_csv(args.clean_data)

# Separa,os las variables Dependeientes de la variable independeiente
#X = clean_data.drop(columns=['Potability'])
#y = clean_data['Potability']

# Split the dataset into training and testing sets
#X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=args.split_ratio_train , random_state=42)
train_data, test_data = train_test_split(clean_data, train_size=args.split_ratio_train , random_state=42)

#train_data = pd.concat([X_train,y_train],axis=1)
#test_data = pd.concat([X_test,y_test],axis=1)

# Guardamos los datasets ya separados en sus respectivos outputs
train_data.to_csv(args.data_train, index=False)
test_data.to_csv(args.data_test, index=False)